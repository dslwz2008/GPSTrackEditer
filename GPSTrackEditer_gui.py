# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GPSTrackEditer.ui'
#
# Created: Wed Nov 19 18:37:09 2014
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
        self.action_ZoonIn = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/ZoomInTool_B_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_ZoonIn.setIcon(icon1)
        self.action_ZoonIn.setObjectName(_fromUtf8("action_ZoonIn"))
        self.action_ZoomOut = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/ZoomOutTool_B_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_ZoomOut.setIcon(icon2)
        self.action_ZoomOut.setObjectName(_fromUtf8("action_ZoomOut"))
        self.action_Pan = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/PanTool_B_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_Pan.setIcon(icon3)
        self.action_Pan.setObjectName(_fromUtf8("action_Pan"))
        self.menu.addAction(self.action_OpenGPXFile)
        self.menu.addSeparator()
        self.menu.addAction(self.action_Exit)
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.action_tbOpenGPXFile)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Pan)
        self.toolBar.addAction(self.action_ZoonIn)
        self.toolBar.addAction(self.action_ZoomOut)

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
        self.action_ZoonIn.setText(QtGui.QApplication.translate("MainWindow", "放大", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoonIn.setToolTip(QtGui.QApplication.translate("MainWindow", "放大", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setText(QtGui.QApplication.translate("MainWindow", "缩小", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ZoomOut.setToolTip(QtGui.QApplication.translate("MainWindow", "缩小", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Pan.setText(QtGui.QApplication.translate("MainWindow", "漫游", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Pan.setToolTip(QtGui.QApplication.translate("MainWindow", "漫游", None, QtGui.QApplication.UnicodeUTF8))

import GPSTrackEditer_rc
