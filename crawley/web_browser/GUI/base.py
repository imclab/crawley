# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created: Mon Oct 24 23:46:32 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1132, 671)
        self.centralwidget = QtGui.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.centralwidget.setFont(font)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setMargin(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bt_back = QtGui.QPushButton(self.frame)
        self.bt_back.setText("")
        self.bt_back.setObjectName("bt_back")
        self.horizontalLayout_5.addWidget(self.bt_back)
        self.bt_ahead = QtGui.QPushButton(self.frame)
        self.bt_ahead.setText("")
        self.bt_ahead.setObjectName("bt_ahead")
        self.horizontalLayout_5.addWidget(self.bt_ahead)
        self.bt_reload = QtGui.QPushButton(self.frame)
        self.bt_reload.setText("")
        self.bt_reload.setObjectName("bt_reload")
        self.horizontalLayout_5.addWidget(self.bt_reload)
        self.bt_start = QtGui.QPushButton(self.frame)
        self.bt_start.setObjectName("bt_start")
        self.horizontalLayout_5.addWidget(self.bt_start)
        self.bt_open = QtGui.QPushButton(self.frame)
        self.bt_open.setObjectName("bt_open")
        self.horizontalLayout_5.addWidget(self.bt_open)
        self.bt_save = QtGui.QPushButton(self.frame)
        self.bt_save.setObjectName("bt_save")
        self.horizontalLayout_5.addWidget(self.bt_save)
        self.bt_configure = QtGui.QPushButton(self.frame)
        self.bt_configure.setObjectName("bt_configure")
        self.horizontalLayout_5.addWidget(self.bt_configure)
        self.bt_settings = QtGui.QPushButton(self.frame)
        self.bt_settings.setObjectName("bt_settings")
        self.horizontalLayout_5.addWidget(self.bt_settings)
        self.bt_run = QtGui.QPushButton(self.frame)
        self.bt_run.setObjectName("bt_run")
        self.horizontalLayout_5.addWidget(self.bt_run)
        self.tb_url = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_url.sizePolicy().hasHeightForWidth())
        self.tb_url.setSizePolicy(sizePolicy)
        self.tb_url.setSizeIncrement(QtCore.QSize(0, 0))
        self.tb_url.setObjectName("tb_url")
        self.horizontalLayout_5.addWidget(self.tb_url)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.tab_pages = QtGui.QTabWidget(self.frame)
        self.tab_pages.setTabsClosable(True)
        self.tab_pages.setMovable(True)
        self.tab_pages.setObjectName("tab_pages")
        self.gridLayout.addWidget(self.tab_pages, 5, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_pages.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Crawley Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_start.setText(QtGui.QApplication.translate("MainWindow", "Start Project", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_open.setText(QtGui.QApplication.translate("MainWindow", "Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_save.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_configure.setText(QtGui.QApplication.translate("MainWindow", "Configure", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_settings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_run.setText(QtGui.QApplication.translate("MainWindow", "Run Crawler", None, QtGui.QApplication.UnicodeUTF8))
