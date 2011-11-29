import os.path
import shutil

import panacea
import crawley

from multiprocessing import Process
from eventlet.green.threading import Thread as GreenThread
from crawley.multiprogramming.threads import KThread
from crawley.multiprogramming.collections import WorkersList

from crawley.utils import generate_template, get_full_template_path, has_valid_attr
from crawley.persistance import Entity, UrlEntity, setup
from crawley.persistance.relational.databases import session as database_session

from crawley.persistance.documents import json_session, JSONDocument
from crawley.persistance.documents import documents_entities, xml_session, XMLDocument
from crawley.persistance.documents import csv_session, CSVDocument

from crawley.persistance.nosql.mongo import mongo_session, MongoEntity
from crawley.persistance.nosql.couch import couch_session, CouchEntity
from crawley.persistance.relational.connectors import connectors


worker_type = { 'greenlets' : GreenThread, 'threads' : KThread }

class BaseProject(object):
    """
        Base of all crawley's projects
    """

    def set_up(self, project_name):
        """
            Setups a crawley project
        """

        self._create_module(project_name)
        self._write_meta_data(project_name)
        generate_template("settings", project_name, project_name)

        self.project_dir = os.path.join(project_name, project_name)
        self._create_module(self.project_dir)

    def _write_meta_data(self, directory_module):

        with open(get_full_template_path("metadata")) as f:
            data = f.read()

        data = data % { 'version' : crawley.__version__, 'type' : self.name }

        with open(os.path.join(directory_module, "__init__.py"), "w") as f:
            f.write(data)

    def _create_module(self, name):
        """
            Generates a python module with the given name
        """

        if not os.path.exists(name):

            shutil.os.mkdir(name)
            f = open(os.path.join(name, "__init__.py"), "w")
            f.close()

    def syncdb(self, syncb_command):
        """
            Checks for storages configuration in the settings.py file
        """

        self.connector = None
        syncb_command.sessions = []

        documents_sessions = { 'JSON_DOCUMENT' : json_session,
                               'XML_DOCUMENT' : xml_session,
                               'CSV_DOCUMENT' : csv_session,
                               'MONGO_DB_HOST' : mongo_session, 
                               'COUCH_DB_HOST' : couch_session,
                             }

        for storage_name, session in documents_sessions.iteritems():

            if has_valid_attr(syncb_command.settings, storage_name):

                session.set_up(syncb_command.settings, storage_name)
                syncb_command.sessions.append(session)

        if has_valid_attr(syncb_command.settings, "DATABASE_ENGINE"):

            syncb_command.sessions.append(database_session)
            self.connector = connectors[syncb_command.settings.DATABASE_ENGINE](syncb_command.settings)

    def _setup_entities(self, entities, settings):

        panacea.metadata.bind = self.connector.get_connection_string()
        panacea.metadata.bind.echo = settings.SHOW_DEBUG_INFO

        setup(panacea.entities)

    def run(self, run_command, crawlers):

        workers = WorkersList()

        for crawler_class in crawlers:

            crawler = crawler_class(sessions=run_command.syncdb.sessions, settings=run_command.settings)

            pool_type = getattr(run_command.settings, 'POOL', 'greenlets')
            worker_class = worker_type[pool_type]

            worker = worker_class(target=crawler.start)
            workers.append(worker)

        workers.start()
        workers.waitall()

        for session in run_command.syncdb.sessions:
            session.close()