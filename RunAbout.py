#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pywisetableabout import *


class PyWiseAbout(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonClose.clicked.connect(self.closeabout)

    def closeabout(self):
        self.close()
