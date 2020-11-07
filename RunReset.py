#!/usr/bin/env python
# -*- coding: utf-8 -*-


from resetconfirm import *


class Reset(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonOK.clicked.connect(self.confirm)
        self.ui.buttonCancel.clicked.connect(self.cancel)

    def confirm(self):
        self.accept()

    def cancel(self):
        self.close()
