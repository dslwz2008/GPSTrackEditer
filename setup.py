# -*-coding:utf-8-*-
# Authoe: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

from distutils.core import setup
import py2exe

py2exe_options = {
    "includes":["sip", "PyQt4.QtCore", "PyQt4.QtGui",
                "PyQt4.QtNetwork", "PyQt4.QtXml"],
}

setup(
    windows=["TrackEditer.py"],
    options={
        'py2exe':py2exe_options
    }
)