# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GPSTrackEditer.ui'
#
# Created: Wed Nov 19 15:40:53 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_OpenGPXFile = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/GenericOpen_B_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_OpenGPXFile.setIcon(icon)
        self.action_OpenGPXFile.setObjectName(_fromUtf8("action_OpenGPXFile"))
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName(_fromUtf8("action_Exit"))
        self.action_tbOpenGPXFile = QtGui.QAction(MainWindow)
        self.action_tbOpenGPXFile.setIcon(icon)
        self.action_tbOpenGPXFile.setObjectName(_fromUtf8("action_tbOpenGPXFile"))
        self.menu.addAction(self.action_OpenGPXFile)
        self.menu.addSeparator()
        self.menu.addAction(self.action_Exit)
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.action_tbOpenGPXFile)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "文件", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OpenGPXFile.setText(QtGui.QApplication.translate("MainWindow", "打开gpx文件", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setText(QtGui.QApplication.translate("MainWindow", "退出", None, QtGui.QApplication.UnicodeUTF8))
        self.action_tbOpenGPXFile.setText(QtGui.QApplication.translate("MainWindow", "打开GPX文件", None, QtGui.QApplication.UnicodeUTF8))
        self.action_tbOpenGPXFile.setToolTip(QtGui.QApplication.translate("MainWindow", "点击打开GPX文件", None, QtGui.QApplication.UnicodeUTF8))

import GPSTrackEditer_rc
