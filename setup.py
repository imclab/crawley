#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from crawley import __version__

setup(
    name="crawley",
    version=__version__,
    description="Pythonic Scraping / Crawling FrameWork built On Eventlet",
    author="",
    author_email = "",
    license = "GPL v3",
    keywords = "Scarping Crawling Framework Python",
    include_package_data = True,
    packages=['crawley', 'crawley.manager', 'crawley.conf.project_template'],
    scripts=['crawley/bin/crawley-admin.py'],
    url='',
)