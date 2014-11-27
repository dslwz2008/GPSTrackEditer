# -*-coding:utf-8-*-
# Authoe: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

import shapefile
import csv
import gpxpy
import gpxpy.gpx
from pyproj import Proj

# WGS84 / UTM zone 50N
WKTSTR = '''PROJCS["WGS_1984_UTM_Zone_50N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",117],PARAMETER["scale_factor",0.9996],PARAMETER["false_easting",500000],PARAMETER["false_northing",0],UNIT["Meter",1]]'''
PROJ4STR = '+proj=utm +zone=50 +ellps=WGS84 +datum=WGS84 +units=m +no_defs'

class GPXLoader(object):
    def __init__(self, filename):
        self.points = []
        fh = open(filename, 'r')
        gpx = gpxpy.parse(fh)
        for track in gpx.tracks:
            for seg in track.segments:
                for point in seg.points:
                    # type of point is GPXTrackPoint
                    # only need points
                    self.points.append(point)


    def gen_shapefile(self, shp_filename):
        wrt = shapefile.Writer(shapeType=1) # point
        wrt.autoBalance = 1
        wrt.field('elev', 'N')
        wrt.field('time', 'D')
        for p in self.points:
            proj_func = Proj(PROJ4STR)
            x,y = proj_func(p.longitude, p.latitude)
            #print(x,y)
            wrt.point(x, y)
            wrt.record(p.elevation, p.time)
        wrt.save(shp_filename)

        # write prj file
        prj = open('%s.prj' % shp_filename, 'w')
        prj.write(WKTSTR)
        prj.close()


    def gen_csv(self, csv_filename):
        csvfile = open(csv_filename + '.csv', 'w')
        wrt = csv.writer(csvfile, delimiter=',')
        for p in self.points:
            wrt.writerow([p.longitude, p.latitude, p.elevation, p.time])


if __name__ == '__main__':
    import os.path
    gpx_file = 'data/2013-11-28 13.06.07.gpx'
    loader = GPXLoader(gpx_file)
    basename = os.path.basename(gpx_file).split('.')[0]
    loader.gen_csv(basename)
    loader.gen_shapefile(basename)
