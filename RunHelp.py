#!/usr/bin/env python
# -*- coding: utf-8 -*-


from help import *


class Help(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonClose.clicked.connect(self.closehelp)

    def closehelp(self):
        self.close()
