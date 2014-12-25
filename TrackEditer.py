# -*-coding:utf-8-*-
# Authoe: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from CustomMapTools import *
from GPXTools import *
import os
import os.path
import sys
import imp
import re

from GPSTrackEditer_gui import Ui_MainWindow

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


def main_is_frozen():
    return (hasattr(sys, "frozen") or  # new py2exe
            hasattr(sys, "importers") or  # old py2exe
            imp.is_frozen("__main__"))  # tools/freeze


def get_main_dir():
    if main_is_frozen():
        return os.path.dirname(sys.executable)
    return os.path.dirname(sys.argv[0])


class TrackEditer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(_fromUtf8(u"GPS轨迹编辑"))
        # create map canvas
        self.canvas = QgsMapCanvas()
        self.canvas.show()
        self.canvas.setCanvasColor(Qt.white)
        self.canvas.enableAntiAliasing(True)

        # self.layout = QVBoxLayout(self.frame)
        # self.layout.addWidget((self.canvas))
        self.setCentralWidget(self.canvas)

        # open base image layer
        basemap_name = get_main_dir() + "\\data\\35school.tif"
        baseName = basename(basemap_name)
        self.basemap_layer = QgsRasterLayer(basemap_name, baseName)
        if not self.basemap_layer.isValid():
            QMessageBox.information(None, _fromUtf8(u"错误"), _fromUtf8(u"打开底图失败！"))
            return

        # add layer
        QgsMapLayerRegistry.instance().addMapLayer(self.basemap_layer)
        self.canvas.setExtent(self.basemap_layer.extent())
        # set up map canvas layer set
        self.layer_set = [QgsMapCanvasLayer(self.basemap_layer)]
        self.canvas.setLayerSet(self.layer_set)
        self.track_layer = None
        self.gpx_loader = None

        self.connect(self.action_ZoomIn, SIGNAL("triggered()"), self.zoom_in)
        self.connect(self.action_ZoomOut, SIGNAL("triggered()"), self.zoom_out)
        self.connect(self.action_Pan, SIGNAL("triggered()"), self.pan)
        self.connect(self.action_OpenGPXFile, SIGNAL("triggered()"), self.open_gpx_file)
        self.connect(self.action_tbOpenGPXFile, SIGNAL("triggered()"), self.open_gpx_file)
        self.connect(self.action_Exit, SIGNAL("triggered()"), self.exit)
        self.connect(self.action_SelectByRect, SIGNAL("triggered()"), self.select_by_rect)
        self.connect(self.action_MoveVertex, SIGNAL("triggered()"), self.move_vertex)
        self.connect(self.action_Home, SIGNAL("triggered()"), self.home_view)
        # after track layer has been edited, update csv file
        self.connect(self.canvas, SIGNAL('mapCanvasRefreshed()'), self.update_csv)
        self.connect(self.action_doc, SIGNAL("triggered()"), self.open_doc)
        self.connect(self.action_about, SIGNAL("triggered()"), self.about)

        # create maptools
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
        gpx_filename = QFileDialog.getOpenFileName(self, _fromUtf8(u"请选择gpx文件"), "./data",
                                                   _fromUtf8(u"GPS文件(*.gpx)"))
        if gpx_filename == '':
            return

        gpx_filename = str(gpx_filename)
        # convert gpx to shapefile first
        self.gpx_loader = GPXLoader(gpx_filename)
        baseName = basename(gpx_filename)
        dirname = os.path.dirname(gpx_filename)
        # generate shapefile first
        self.gpx_loader.gen_shapefile()
        self.gpx_loader.gen_csv()

        # has already load track layer, delete first
        if self.track_layer is not None:
            trklyr_name = '_'.join(re.findall('\d+', str(self.track_layer.name())))
            for name in QgsMapLayerRegistry.instance().mapLayers():
                if name.indexOf(trklyr_name) != -1:  # found
                    # remove from manager
                    QgsMapLayerRegistry.instance().removeMapLayer(name)
                    # remove from local layer set
                    self.layer_set.remove(self.layer_set[0])
                    self.track_layer = None
                    break
            print(QgsMapLayerRegistry.instance().count())

        # load shapefile
        shp_filename = '%s/%s.%s' % (dirname, baseName, 'shp')
        self.track_layer = QgsVectorLayer(shp_filename, baseName, "ogr")
        if not self.track_layer.isValid():
            return
        QgsMapLayerRegistry.instance().addMapLayer(self.track_layer)
        self.layer_set.insert(0, QgsMapCanvasLayer(self.track_layer))
        self.canvas.setLayerSet(self.layer_set)
        self.canvas.setExtent(self.track_layer.extent())
        self.toolRectSelection.setSelectLayer(self.track_layer)
        # maps = QgsMapLayerRegistry.instance().mapLayers()
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
            QMessageBox.information(self, _fromUtf8(u"注意"), _fromUtf8(u"请先选择矢量要素！"))
            return
        self.canvas.setMapTool(self.toolMoveVertex)
        self.toolMoveVertex.setEditLayer(self.track_layer)

    def home_view(self):
        self.canvas.setExtent(self.basemap_layer.extent())
        self.canvas.refresh()

    def open_doc(self):
        import os
        os.startfile(u"GPS室外定位轨迹编辑系统使用说明.html")

    def about(self):
        QMessageBox.information(self, _fromUtf8(u"关于"),
                                _fromUtf8(u"GPSTrackEditer 1.0 版权所有"))

    def update_csv(self):
        if self.canvas.mapTool() == self.toolMoveVertex and \
                        self.track_layer is not None:
            points = []
            # return all features
            fit = self.track_layer.getFeatures(QgsFeatureRequest())
            fet = QgsFeature()
            while fit.nextFeature(fet):
                points.append(fet.geometry().asPoint())
                #print(pnt.x(), pnt.y())
            self.gpx_loader.update_csv(points)


def main(argv):
    # create Qt application
    app = QApplication(argv)

    # get prefix path from env variable
    prefix_path = os.getenv("QGIS_PREFIX")
    if prefix_path is None:
        QMessageBox.information(None, _fromUtf8(u"错误！"), _fromUtf8(u"请先设置QGIS_PREFIX变量"))
        return
    QgsApplication.setPrefixPath(prefix_path, True)
    QgsApplication.initQgis()

    print(QgsApplication.showSettings())
    # create main window
    wnd = TrackEditer()
    wnd.move(100, 100)
    wnd.show()

    retval = app.exec_()

    # exit
    QgsApplication.exitQgis()
    sys.exit(retval)


if __name__ == '__main__':
    main(sys.argv)
    # print(basename('d:/test/abc lll.123'))
    # print(get_main_dir())
