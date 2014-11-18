# -*-coding:utf-8-*-
# Authoe: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

from qgis.core import *

QgsApplication.setPrefixPath("D:/Program Files (x86)/QGIS Valmiera/apps/qgis/bin", True)
QgsApplication.initQgis()

print('before!')
vector = "D:/data/qgis_sample_data/shapefiles/alaska.shp"
vec_layer = QgsVectorLayer(vector, "alaska", "ogr")
if not vec_layer.isValid():
    print('error in load vector layer!')

QgsApplication.exitQgis()
