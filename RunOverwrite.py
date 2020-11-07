#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pywiseoverwriteconfirm import *


class PyWiseOverwrite(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.buttonOK, QtCore.SIGNAL('clicked()'), self.confirm)
        QtCore.QObject.connect(self.ui.buttonCancel, QtCore.SIGNAL('clicked()'), self.cancel)

    def confirm(self):
        self.accept()

    def cancel(self):
        self.close()
