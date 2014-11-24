# -*-coding:utf-8-*-
# Authoe: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from CustomMapTools import *
import os
import sys

from GPSTrackEditer_gui import Ui_MainWindow

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


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
        self.basemap_layer = QgsRasterLayer(basemap_name, baseName)
        if not self.basemap_layer.isValid():
            QMessageBox.information(None, _fromUtf8("错误"), _fromUtf8("打开底图失败！"))
            return

        #add layer
        QgsMapLayerRegistry.instance().addMapLayer(self.basemap_layer)
        self.canvas.setExtent(self.basemap_layer.extent())
        # set up map canvas layer set
        self.layer_set = [ QgsMapCanvasLayer(self.basemap_layer) ]
        self.canvas.setLayerSet(self.layer_set)
        self.track_layer = None

        self.connect(self.action_ZoomIn, SIGNAL("triggered()"), self.zoom_in)
        self.connect(self.action_ZoomOut, SIGNAL("triggered()"), self.zoom_out)
        self.connect(self.action_Pan, SIGNAL("triggered()"), self.pan)
        self.connect(self.action_OpenGPXFile, SIGNAL("triggered()"), self.open_gpx_file)
        self.connect(self.action_tbOpenGPXFile, SIGNAL("triggered()"), self.open_gpx_file)
        self.connect(self.action_Exit, SIGNAL("triggered()"), self.exit)
        self.connect(self.action_SelectByRect, SIGNAL("triggered()"), self.select_by_rect)
        self.connect(self.action_MoveVertex, SIGNAL("triggered()"), self.move_vertex)
        self.connect(self.action_SaveGPSTrack, SIGNAL("triggered()"), self.save_gps_file)
        self.connect(self.action_tbSaveGPSTrack, SIGNAL("triggered()"), self.save_gps_file)

        #create maptools
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(self.action_Pan)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False)
        self.toolZoomIn.setAction(self.action_ZoomIn)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True)
        self.toolZoomOut.setAction(self.action_ZoomOut)
        self.toolRectSelection = RectSelectionMapTool(self.canvas, self.track_layer)
        self.toolRectSelection.setAction(self.action_SelectByRect)
        self.toolMoveVertex = MoveVertexMapTool(self.canvas)
        self.toolMoveVertex.setAction(self.action_MoveVertex)

        self.pan()

    def open_gpx_file(self):
        filename = QFileDialog.getOpenFileName(self, _fromUtf8("请选择gpx文件"), "./data",
                                    _fromUtf8("GPS文件(*.gpx);;Shapefile(*.shp)"))
        if filename is None:
            return

        # convert gpx to shapefile

        #has already load track layer, delete first
        if self.track_layer is not None:
            trklyr_name = self.track_layer.name()
            for name in QgsMapLayerRegistry.instance().mapLayers():
                if name.indexOf(trklyr_name) != -1:#found
                    # remove from manager
                    QgsMapLayerRegistry.instance().removeMapLayer(name)
                    # remove from local layer set
                    self.layer_set.remove(self.layer_set[0])
                    self.track_layer = None
                    break
            print(QgsMapLayerRegistry.instance().count())

        # load shapefile
        fileinfo = QFileInfo(filename)
        baseName = fileinfo.baseName()
        self.track_layer = QgsVectorLayer(filename, baseName, "ogr")
        if not self.track_layer.isValid():
            return
        QgsMapLayerRegistry.instance().addMapLayer(self.track_layer)
        self.layer_set.insert(0, QgsMapCanvasLayer(self.track_layer))
        self.canvas.setLayerSet(self.layer_set)
        self.canvas.setExtent(self.track_layer.extent())
        self.toolRectSelection.setSelectLayer(self.track_layer)
        #maps = QgsMapLayerRegistry.instance().mapLayers()
        #print(maps)
        print(QgsMapLayerRegistry.instance().count())
        print(self.track_layer.dataProvider().capabilitiesString())

    def exit(self):
        self.close()

    def zoom_in(self):
        self.canvas.setMapTool(self.toolZoomIn)

    def zoom_out(self):
        self.canvas.setMapTool(self.toolZoomOut)

    def pan(self):
        self.canvas.setMapTool(self.toolPan)

    def select_by_rect(self):
        self.canvas.setMapTool(self.toolRectSelection)

    def move_vertex(self):
        if self.track_layer is None or \
            self.track_layer.selectedFeatureCount() == 0:
            QMessageBox.information(self, _fromUtf8("注意"), _fromUtf8("请先选择矢量要素！"))
            return
        self.canvas.setMapTool(self.toolMoveVertex)
        self.toolMoveVertex.setEditLayer(self.track_layer)

    def save_gps_file(self):
        # filename = QFileDialog.getSaveFileName(self, _fromUtf8("请保存gpx文件"), "./data",
        #                             _fromUtf8("GPS文件(*.gpx)"))
        # if filename is None:
        #     return
        pass


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
