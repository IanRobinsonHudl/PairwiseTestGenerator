# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pywisetablehelp.ui'
#
# Created: Wed Jan 03 15:09:21 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(404, 343)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Dialog.setFont(font)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.buttonClose = QtGui.QPushButton(Dialog)
        self.buttonClose.setMaximumSize(QtCore.QSize(75, 23))
        self.buttonClose.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonClose.setObjectName(_fromUtf8("buttonClose"))
        self.verticalLayout_2.addWidget(self.buttonClose)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Help", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; font-weight:600; color:#000000;\">PyWiseCL is an open source, cross platform Python tool for creating pairwise test case combinations.<br />It is written in Python 2.7.5 and requires that the Metacomm all_pairs 2.0.1 Python library is installed.<br /><br />Add factors and options to the Factors tab.  For example, for a test on a font selection dialog, the factors and options might be: -<br />---<br />Type - Times New Roman,Courier,Arial,Serif<br />Size - 8,10,12,14<br />Style - Bold,Underline,Italic<br />---<br />Any factors with no options or options with no factors will be excluded from the analysis and when saving to file.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; font-weight:600; color:#000000;\">PyWiseCL will output an efficient set of pairwise test combinations to the Results tab.  From here they can be copied or exported to Excel.<br /><br />Constraints can also be applied to the pairwise analysis.<br />Constraints are invalid combinations of items that can be excluded from the analysis.<br />They are applied on the Constraints tab, dynamically updating based on the contents of the Factors tab.  Each row represents a separate constraint.<br />So for example if Arial and Bold represent an invalid pair, the constraint should look like this:<br />---<br />Arial, -, Bold<br />---<br />Multiple constraints may be specified with each containing a minimum of 2 items.  More than 2 items can also be specified:<br />---</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; font-weight:600; color:#000000;\">Arial, -, Bold<br />Times New Roman, 10, Bold<br />---</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; font-weight:600; color:#000000;\">Any constraints with less than one option selected will be excluded from the analysis and when saving to file.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; font-weight:600; color:#000000;\">Click Generate Pairwise Analysis to run the analysis.  Results are output to the Results tab where they can be exported directly to file, or copy, pasted into a spreadsheet.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; font-weight:600; color:#000000;\">Click Reset to reset the tables.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; font-weight:600; color:#000000;\">Open and Save files via the tool bar.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; font-weight:600; color:#000000;\"><br />KNOWN BUG: If you have more constraints than there are rows of elements, e.g. 8 constraints and only 7 rows of elements<br />then the 7th constraint does not get applied</span></p></body></html>", None))
        self.buttonClose.setText(_translate("Dialog", "Close", None))

