# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pywisetablemain.ui'
#
# Created: Mon Mar 26 16:55:01 2018
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(635, 449)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tablePairs = QtGui.QTableWidget(self.tab)
        self.tablePairs.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked)
        self.tablePairs.setDragEnabled(False)
        self.tablePairs.setAlternatingRowColors(True)
        self.tablePairs.setRowCount(11)
        self.tablePairs.setColumnCount(10)
        self.tablePairs.setObjectName(_fromUtf8("tablePairs"))
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 127))
        self.tablePairs.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tablePairs.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tablePairs.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablePairs.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablePairs.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablePairs.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablePairs.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablePairs.setItem(0, 5, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablePairs.setItem(0, 6, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablePairs.setItem(0, 7, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablePairs.setItem(0, 8, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablePairs.setItem(0, 9, item)
        self.gridLayout_2.addWidget(self.tablePairs, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonAddFactor = QtGui.QPushButton(self.tab)
        self.buttonAddFactor.setMaximumSize(QtCore.QSize(51, 23))
        self.buttonAddFactor.setObjectName(_fromUtf8("buttonAddFactor"))
        self.horizontalLayout.addWidget(self.buttonAddFactor)
        self.buttonAddOption = QtGui.QPushButton(self.tab)
        self.buttonAddOption.setMaximumSize(QtCore.QSize(51, 23))
        self.buttonAddOption.setObjectName(_fromUtf8("buttonAddOption"))
        self.horizontalLayout.addWidget(self.buttonAddOption)
        spacerItem = QtGui.QSpacerItem(388, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableConstraints = QtGui.QTableWidget(self.tab_2)
        self.tableConstraints.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableConstraints.setRowCount(0)
        self.tableConstraints.setColumnCount(0)
        self.tableConstraints.setObjectName(_fromUtf8("tableConstraints"))
        self.gridLayout_3.addWidget(self.tableConstraints, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.buttonAdd = QtGui.QPushButton(self.tab_2)
        self.buttonAdd.setEnabled(False)
        self.buttonAdd.setObjectName(_fromUtf8("buttonAdd"))
        self.horizontalLayout_4.addWidget(self.buttonAdd)
        spacerItem1 = QtGui.QSpacerItem(338, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tableResults = QtGui.QTableWidget(self.tab_3)
        self.tableResults.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableResults.setAlternatingRowColors(True)
        self.tableResults.setObjectName(_fromUtf8("tableResults"))
        self.tableResults.setColumnCount(0)
        self.tableResults.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableResults, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.buttonExcel = QtGui.QPushButton(self.tab_3)
        self.buttonExcel.setEnabled(False)
        self.buttonExcel.setObjectName(_fromUtf8("buttonExcel"))
        self.horizontalLayout_5.addWidget(self.buttonExcel)
        spacerItem2 = QtGui.QSpacerItem(448, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.buttonGenerate = QtGui.QPushButton(self.centralwidget)
        self.buttonGenerate.setMaximumSize(QtCore.QSize(137, 23))
        self.buttonGenerate.setObjectName(_fromUtf8("buttonGenerate"))
        self.horizontalLayout_2.addWidget(self.buttonGenerate)
        spacerItem3 = QtGui.QSpacerItem(148, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.buttonClear = QtGui.QPushButton(self.centralwidget)
        self.buttonClear.setMaximumSize(QtCore.QSize(75, 23))
        self.buttonClear.setObjectName(_fromUtf8("buttonClear"))
        self.horizontalLayout_2.addWidget(self.buttonClear)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.labelMessage = QtGui.QLabel(self.centralwidget)
        self.labelMessage.setText(_fromUtf8(""))
        self.labelMessage.setObjectName(_fromUtf8("labelMessage"))
        self.verticalLayout.addWidget(self.labelMessage)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionFactors = QtGui.QAction(MainWindow)
        self.actionFactors.setObjectName(_fromUtf8("actionFactors"))
        self.actionConstraints = QtGui.QAction(MainWindow)
        self.actionConstraints.setObjectName(_fromUtf8("actionConstraints"))
        self.actionResults = QtGui.QAction(MainWindow)
        self.actionResults.setObjectName(_fromUtf8("actionResults"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuView.addAction(self.actionFactors)
        self.menuView.addAction(self.actionConstraints)
        self.menuView.addAction(self.actionResults)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.tablePairs)
        MainWindow.setTabOrder(self.tablePairs, self.buttonAddFactor)
        MainWindow.setTabOrder(self.buttonAddFactor, self.buttonAddOption)
        MainWindow.setTabOrder(self.buttonAddOption, self.tableConstraints)
        MainWindow.setTabOrder(self.tableConstraints, self.buttonAdd)
        MainWindow.setTabOrder(self.buttonAdd, self.tableResults)
        MainWindow.setTabOrder(self.tableResults, self.buttonExcel)
        MainWindow.setTabOrder(self.buttonExcel, self.buttonGenerate)
        MainWindow.setTabOrder(self.buttonGenerate, self.buttonClear)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PyWiseCL v4.0", None))
        item = self.tablePairs.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Factor Name", None))
        item = self.tablePairs.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Option 1", None))
        item = self.tablePairs.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Option 2", None))
        item = self.tablePairs.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Option 3", None))
        item = self.tablePairs.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Option 4", None))
        item = self.tablePairs.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Option 5", None))
        item = self.tablePairs.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Option 6", None))
        item = self.tablePairs.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Option 7", None))
        item = self.tablePairs.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Option 8", None))
        item = self.tablePairs.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Option 9", None))
        item = self.tablePairs.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Option 10", None))
        item = self.tablePairs.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Factor 1", None))
        item = self.tablePairs.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Factor 2", None))
        item = self.tablePairs.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Factor 3", None))
        item = self.tablePairs.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Factor 4", None))
        item = self.tablePairs.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Factor 5", None))
        item = self.tablePairs.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Factor 6", None))
        item = self.tablePairs.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Factor 7", None))
        item = self.tablePairs.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Factor 8", None))
        item = self.tablePairs.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Factor 9", None))
        item = self.tablePairs.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Factor 10", None))
        __sortingEnabled = self.tablePairs.isSortingEnabled()
        self.tablePairs.setSortingEnabled(False)
        self.tablePairs.setSortingEnabled(__sortingEnabled)
        self.buttonAddFactor.setText(_translate("MainWindow", "+ Factor", None))
        self.buttonAddOption.setText(_translate("MainWindow", "+ Option", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "&Factors", None))
        self.buttonAdd.setText(_translate("MainWindow", "&Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "&Constraints", None))
        self.buttonExcel.setText(_translate("MainWindow", "&Excel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "&Test Cases", None))
        self.buttonGenerate.setText(_translate("MainWindow", "&Generate Pairwise Analysis", None))
        self.buttonClear.setText(_translate("MainWindow", "&Reset", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help", None))
        self.menuView.setTitle(_translate("MainWindow", "&View", None))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionFactors.setText(_translate("MainWindow", "Factors", None))
        self.actionConstraints.setText(_translate("MainWindow", "Constraints", None))
        self.actionResults.setText(_translate("MainWindow", "Test Cases", None))
        self.actionCopy.setText(_translate("MainWindow", "Copy", None))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        self.actionPaste.setText(_translate("MainWindow", "Paste", None))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

import Resource_Files_rc
