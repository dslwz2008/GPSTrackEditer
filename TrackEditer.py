# -*-coding:utf-8-*-
# Authoe: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import os
import sys

from GPSTrackEditer_gui import Ui_MainWindow

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


#global variables



class TrackEditer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(_fromUtf8("GPS轨迹查询"))
        # create map canvas
        self.canvas = QgsMapCanvas()
        self.canvas.show()
        self.canvas.setCanvasColor(Qt.white)
        self.canvas.enableAntiAliasing(True)

        # self.layout = QVBoxLayout(self.frame)
        # self.layout.addWidget((self.canvas))
        self.setCentralWidget(self.canvas)

        # open base image layer
        basemap_name = os.getcwd() + "/data/35school.tif"
        fileinfo = QFileInfo(basemap_name)
        baseName = fileinfo.baseName()
        basemap_layer = QgsRasterLayer(basemap_name, baseName)
        if not basemap_layer.isValid():
            QMessageBox.information(None, _fromUtf8("错误"), _fromUtf8("打开底图失败！"))
            return

        #add layer
        QgsMapLayerRegistry.instance().addMapLayer(basemap_layer)
        self.canvas.setExtent(basemap_layer.extent())
        # set up map canvas layer set
        self.canvas.setLayerSet([ QgsMapCanvasLayer(basemap_layer) ])

        self.connect(self.action_ZoonIn, SIGNAL("triggered()"), self.zoom_in)
        self.connect(self.action_ZoomOut, SIGNAL("triggered()"), self.zoom_out)
        self.connect(self.action_Pan, SIGNAL("triggered()"), self.pan)

        #create maptools
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(self.action_Pan)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False)
        self.toolZoomIn.setAction(self.action_ZoonIn)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True)
        self.toolZoomOut.setAction(self.action_ZoomOut)

        self.pan()

    def zoom_in(self):
        self.canvas.setMapTool(self.toolZoomIn)

    def zoom_out(self):
        self.canvas.setMapTool(self.toolZoomOut)

    def pan(self):
        self.canvas.setMapTool(self.toolPan)


def main(argv):
    #create Qt application
    app = QApplication(argv)

    # get prefix path from env variable
    prefix_path = os.getenv("QGIS_PREFIX")
    if prefix_path is None:
        QMessageBox.information(None, _fromUtf8("错误！"), _fromUtf8("请先设置QGIS_PREFIX变量"))
        return
    QgsApplication.setPrefixPath(prefix_path, True)
    QgsApplication.initQgis()

    print(QgsApplication.showSettings())
    #create main window
    wnd = TrackEditer()
    wnd.move(100, 100)
    wnd.show()

    retval = app.exec_()

    # exit
    QgsApplication.exitQgis()
    sys.exit(retval)


if __name__ == '__main__':
    main(sys.argv)
