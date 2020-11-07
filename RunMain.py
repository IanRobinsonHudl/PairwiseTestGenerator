#!/usr/bin/env python
# -*- coding: utf-8 -*-


from allpairspy import AllPairs
import os
import simplejson
import sys
import time
import xlwt
import RunAbout, RunReset, RunHelp, RunOverwrite, helpers
from main import *
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication


class MyComboBox(QtWidgets.QComboBox):
    # dynamically created combobox for constraints table(i.e. created on the fly)
    # connects the combobox to the save_constraints method to allow for auto saving of constraints to data model
    def __init__(self):
        QtWidgets.QComboBox.__init__(self)
        self.currentIndexChanged.connect(self.update)
        #self.connect(self, QtCore.SIGNAL('currentIndexChanged(int)'), self.update)

    def update(self):
        myapp.save_constraints()


class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionSave.triggered.connect(self.save_table)
        self.ui.actionOpen.triggered.connect(self.load_into_table)
        self.ui.actionCopy.triggered.connect(self.copy)
        self.ui.actionPaste.triggered.connect(self.paste)
        self.ui.actionFactors.triggered.connect(self.goto_factors)
        self.ui.actionConstraints.triggered.connect(self.goto_constraints)
        self.ui.actionResults.triggered.connect(self.goto_results)
        self.ui.actionHelp.triggered.connect(self.help)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.buttonClear.clicked.connect(self.clear_table)
        self.ui.buttonGenerate.clicked.connect(self.generate_analysis)
        self.ui.buttonAdd.clicked.connect(self.add_constraint)
        self.ui.buttonExcel.clicked.connect(self.excel_export)
        self.ui.tablePairs.itemChanged.connect(self.build_factors_options)
        self.ui.actionExit.triggered.connect(self.closedialog)
        self.ui.buttonAddFactor.clicked.connect(self.add_factor)
        self.ui.buttonAddOption.clicked.connect(self.add_option)

        self.auto_save_schema = {
            'factor_options': [],
            'constraints': []
        }
        self.processed_pairs = []  # processed set of options for use in pairwise analysis
        self.constraints_exist = False  # used when adding constraints.  If they exist then don't add the headings again
        self.clip = QApplication.clipboard()  # clipboard for copying results table data
        self.font = QtGui.QFont()

    def keyPressEvent(self, e):
        # method used for trapping key events for copy, paste and delete actions
        if e.modifiers() and QtCore.Qt.ControlModifier:
            if e.key() == QtCore.Qt.Key_C:
                self.copy()
            elif e.key() == QtCore.Qt.Key_V:
                self.paste()
        if e.key() == QtCore.Qt.Key_Backspace or e.key() == QtCore.Qt.Key_Delete:
            self.delete()

    def copy_action(self, table):
        # performs action of copying items from selected table to clipboard
        selected = table.selectedRanges()
        try:
            s = ""
            for row in range(selected[0].topRow(), selected[0].bottomRow() + 1):
                for col in range(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                    try:
                        s += str(table.item(row, col).text()) + "\t"
                    except AttributeError:
                        s += "\t"
                s = s[:-1] + "\n"
            self.clip.setText(s)
        except Exception:
            pass

    def copy(self):
        # works out which table to copy items from
        if self.ui.tabWidget.currentIndex() == 2:
            table = self.ui.tableResults
            self.copy_action(table)
        elif self.ui.tabWidget.currentIndex() == 0:
            table = self.ui.tablePairs
            self.copy_action(table)

    def paste(self):
        # paste method for pasting in factors and options
        table = self.ui.tablePairs
        selected = table.selectedRanges()
        try:
            first_row = selected[0].topRow()
            first_col = selected[0].leftColumn()
            rows = len(self.clip.text().split('\n')) - 1
            while table.rowCount() < rows:
                self.add_option()  # adds more rows if more options exist than the default of 10
            for r, row in enumerate(self.clip.text().split('\n')):
                columns = len(row.split('\t'))
                while table.columnCount() < columns:
                    self.add_factor()  # adds more columns if more factors exist than the default of 10
                for c, text in enumerate(row.split('\t')):
                    table.setItem(first_row + r, first_col + c, QtWidgets.QTableWidgetItem(text))
        except Exception:
            pass

    def delete(self):
        # delete method for deleting items from factors table
        table = self.ui.tablePairs
        selected = table.selectedRanges()
        for row in range(selected[0].topRow(), selected[0].bottomRow() + 1):
            for col in range(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                item = QtWidgets.QTableWidgetItem('')
                table.setItem(row, col, item)

    def excel_export(self):
        # method allows table to be exported to excel
        table = self.ui.tableResults
        data = []
        for row in range(table.rowCount()):
            data_line = []
            for col in range(table.columnCount()):
                cell_text = str(table.item(row, col).text())
                data_line.append(cell_text)
            data.append(data_line)

        wb = xlwt.Workbook()
        ws = wb.add_sheet('PairWise Results')
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                ws.write(i, j, col)
        if table.rowCount() != 0 and table.columnCount() != 0:
            timestamp = time.strftime("%Y%m%d%H%M%S")
            outfile_name = 'pairwiseresults' + str(timestamp) + '.xls'
            try:
                wb.save(outfile_name)
                self.ui.labelMessage.setStyleSheet('color: green')
                self.ui.labelMessage.setText('Result exported to: ' + str(outfile_name))
            except Exception:
                self.ui.labelMessage.setStyleSheet('color: red')
                self.ui.labelMessage.setText('Problem exporting to excel')
                raise
        else:
            self.ui.labelMessage.setStyleSheet('color: red')
            self.ui.labelMessage.setText('No results to export')

    def help(self):
        pwhelp = RunHelp.Help(self)
        pwhelp.show()

    def about(self):
        pwabout = RunAbout.About(self)
        pwabout.show()

    @staticmethod
    def closedialog(self):
        sys.exit(0)

    def closeEvent(self, event):
        # required for when closing app via the X button.  Otherwise for some reason it crashes
        sys.exit(0)

    def goto_factors(self):
        self.ui.tabWidget.setCurrentIndex(0)

    def goto_constraints(self):
        self.ui.tabWidget.setCurrentIndex(1)

    def goto_results(self):
        self.ui.tabWidget.setCurrentIndex(2)

    def build_factors_options(self):
        # saves factors and options on the fly for use in analysis
        self.auto_save_schema['factor_options'] = []
        table = self.ui.tablePairs
        for column in range(table.columnCount()):
            factor = {}
            options = []
            for row in range(table.rowCount()):
                cell = table.item(row, column)
                if cell is not None:
                    cell_content = str(cell.text())
                    if len(cell_content) != 0:
                        if row == 0:
                            self.font.setBold(True)
                            cell.setFont(self.font)
                            factor['factorName'] = cell_content
                        else:
                            options.append(cell_content)
            # block ensures only complete factor/options are included in auto_save
            if options and not factor:
                pass
            elif factor and not options:
                pass
            else:
                if options:
                    factor['options'] = options
                if factor:
                    self.auto_save_schema['factor_options'].append(factor)
                    self.ui.buttonAdd.setEnabled(True)  # if factor/options exist then enable the constraints add button
            if not self.auto_save_schema['factor_options']:  # if all factors and options deleted then disable the constraints add button
                self.ui.buttonAdd.setEnabled(False)

        self.update_constraints()  # after table interacted with, update constraints with new factor/options

    def add_factor(self):
        # adds a new column to the factors table
        table = self.ui.tablePairs
        columns = table.columnCount()
        table.insertColumn(columns)
        fact_name = 'Factor ' + str(columns + 1)
        table.setHorizontalHeaderItem(columns, QtWidgets.QTableWidgetItem(fact_name))

    def add_option(self):
        # adds a new row to the factors table
        table = self.ui.tablePairs
        rows = table.rowCount()
        table.insertRow(rows)
        op_name = 'Option ' + str(rows)
        table.setVerticalHeaderItem(rows, QtWidgets.QTableWidgetItem(op_name))

    def update_constraints(self):
        # updates existing constraints with new factors/options automatically
        table = self.ui.tableConstraints

        # reset the table and add constraints
        table.setRowCount(0)
        table.setColumnCount(0)
        self.constraints_exist = False

        # once reset, re-add constraints based on save schema
        if not self.auto_save_schema['constraints']:
            self.add_constraint(auto_added=True)
        else:
            for row, constraint in enumerate(self.auto_save_schema['constraints'], 1):
                self.add_constraint(auto_added=True)
                for column, option in enumerate(constraint, 1):
                    cell = table.cellWidget(row, column)
                    if option == '':
                        option = '-'
                    try:
                        if option in self.auto_save_schema['factor_options'][column - 1]['options']:
                            index = cell.findText(option, QtCore.Qt.MatchFixedString)
                            cell.setCurrentIndex(index)
                        else:
                            cell.setCurrentIndex(0)
                            self.ui.labelMessage.setStyleSheet('color: green')
                            self.ui.labelMessage.setText('Factors and/or options have been modified.  '
                                                         'Check constraints are still correct')
                    except Exception:
                        raise

    def save_constraints(self):
        # saves constraints on the fly for use in analysis
        table = self.ui.tableConstraints
        self.auto_save_schema['constraints'] = []
        for row in range(table.rowCount()):
            constraint = []
            for column in range(table.columnCount()):
                if row != 0:
                    cell = table.cellWidget(row, column)
                    if cell is not None:
                        option = str(cell.currentText())
                        if option == '-':
                            option = ''
                        constraint.append(option)
            if row != 0:
                # check that constraint contains 2 or more selected items. If not then constraint not saved
                count = 0
                for i in constraint:
                    if i != '':
                        count += 1
                if count > 1:
                    if constraint not in self.auto_save_schema['constraints']:
                        self.auto_save_schema['constraints'].append(constraint)

    def add_constraint(self, auto_added=False):
        # auto_added parameter ensures that error message is only displayed when the Add button
        table = self.ui.tableConstraints
        if not self.constraints_exist:  # if constraints don't exist
            if self.auto_save_schema['factor_options']:  # if factors/options have been added, add title row and new constraint row
                table.insertColumn(0)
                table.insertRow(0)
                table.insertRow(1)
                item = QtWidgets.QTableWidgetItem('Constraint')
                table.setItem(0, 0, item)
                self.font.setBold(True)
                item.setFont(self.font)
                for col, factor in enumerate(self.auto_save_schema['factor_options'], 1):
                    item = QtWidgets.QTableWidgetItem(factor['factorName'])
                    item.setFont(self.font)
                    table.insertColumn(col)
                    table.setItem(0, col, item)
                    for row in range(table.rowCount()):
                        if row != 0:
                            # set constraint title column
                            item = QtWidgets.QTableWidgetItem('Constraint ' + str(1))
                            table.setItem(row, 0, item)
                            # set constraint combo boxes
                            combobox = MyComboBox()
                            combobox.addItem('-')
                            combobox.addItems(factor['options'])
                            table.setCellWidget(row, col, combobox)
                            self.constraints_exist = True
            elif not self.auto_save_schema['factor_options'] and auto_added == False: # ensures error only displayed when add button is used and not when auto-updating the constraints
                self.ui.labelMessage.setStyleSheet('color: red')
                self.ui.labelMessage.setText('No factors have been defined.  Factor must contain both a name and options')
        else:  # runs if constraints do exist.  I.e. only add a constraint row and not a heading row
            rows = table.rowCount()
            table.insertRow(rows)
            for col, factor in enumerate(self.auto_save_schema['factor_options'], 1):
                # set constraint title column
                item = QtWidgets.QTableWidgetItem('Constraint ' + str(rows))
                table.setItem(rows, 0, item)
                # set constraint combo boxes
                combobox = MyComboBox()
                combobox.addItem('-')
                combobox.addItems(factor['options'])
                table.setCellWidget(rows, col, combobox)

    def save_table(self):
        # saves auto_save_schema to json file
        dialog = QtWidgets.QFileDialog()
        dialog.setDefaultSuffix('json')
        name = dialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", 'Save File', 'pairs', '.json')[0]
        if len(name) == 0:
            pass
        else:
            with open(name, 'w') as outfile:
                simplejson.dump(self.auto_save_schema, outfile, sort_keys=True, indent=4, ensure_ascii=False)
            self.ui.labelMessage.setStyleSheet('color: green')
            self.ui.labelMessage.setText('File successfully saved')

    def load(self, pwfile):
        # used in the load_into_table method.  Inserts factors/options and constraints into relevant table cells
        table = self.ui.tablePairs
        constrainttable = self.ui.tableConstraints
        try:
            with open(pwfile) as data_file:
                data = simplejson.load(data_file)
            # load factors and options
            total_factors = len(data['factor_options'])
            while table.columnCount() < total_factors:
                self.add_factor()  # adds more columns if more factors exist than the default of 10
            for col, factor in enumerate(data['factor_options']):
                fact_item = QtWidgets.QTableWidgetItem(factor['factorName'])
                self.font.setBold(True)
                fact_item.setFont(self.font)
                table.setItem(0, col, fact_item)
                try:
                    total_options = len(factor['options'])
                    while table.rowCount() < total_options:
                        self.add_option()  # adds more rows if more options exist than the default of 10
                    for row, option in enumerate(factor['options'], 1):
                        op_item = QtWidgets.QTableWidgetItem(option)
                        table.setItem(row, col, op_item)
                except Exception:
                    raise
            # load constraints
            if data['constraints']:
                constrainttable.removeRow(1)  # required because otherwise an additional row is added
                for row, constraint in enumerate(data['constraints'], 1):
                    self.add_constraint(auto_added=True)
                    for column, option in enumerate(constraint, 1):
                        cell = constrainttable.cellWidget(row, column)
                        if option == '':
                            option = '-'
                        index = cell.findText(option, QtCore.Qt.MatchFixedString)
                        cell.setCurrentIndex(index)

            self.ui.labelMessage.setStyleSheet('color: green')
            self.ui.labelMessage.setText('File successfully opened')
        except Exception:
            self.ui.labelMessage.setStyleSheet('color: red')
            self.ui.labelMessage.setText('Problem opening file.  Check its contents are correct')
            raise

    def load_into_table(self):
        # select file and load contents. If table contains info then display an overwrite confirmation
        table = self.ui.tablePairs
        constrainttable = self.ui.tableConstraints
        file = QtWidgets.QFileDialog.getOpenFileName()[0]
        if len(file) == 0:
            pass
        elif file.split('.')[-1] != 'json':
            self.ui.labelMessage.setStyleSheet('color: red')
            self.ui.labelMessage.setText('Selected file is not a json file')
        elif os.stat(file).st_size == 0:
            self.ui.labelMessage.setStyleSheet('color: red')
            self.ui.labelMessage.setText('Selected file is empty')
        else:  # check if table contains any factors or options
            table_content = False
            for row in range(table.rowCount()):
                for col in range(table.columnCount()):
                    cell = table.item(row, col)
                    if cell is not None:
                        cell_content = str(cell.text())
                        if len(cell_content) != 0:
                            table_content = True
            if table_content:  # if it does contain factors or options then display overwrite confirmation
                overwrite = RunOverwrite.Overwrite(self)
                overwrite.show()
                if overwrite.exec_():
                    table.clearContents()
                    constrainttable.clearContents()
                    self.ui.tableResults.setRowCount(0)
                    self.ui.tableResults.setColumnCount(0)
                    self.load(file)
                    self.goto_factors()
            else:  # else don't display overwrite confirmation
                self.load(file)
                self.goto_factors()

    def clear_table(self):
        # reset all tables, messages and variables
        overwrite = RunReset.Reset(self)
        overwrite.show()
        if overwrite.exec_():
            self.goto_factors()
            self.ui.tablePairs.clearContents()
            self.ui.tablePairs.setRowCount(11)
            self.ui.tablePairs.setColumnCount(10)
            self.ui.tableResults.setRowCount(0)
            self.ui.tableResults.setColumnCount(0)
            self.ui.labelMessage.setText('')
            self.ui.tableConstraints.setRowCount(0)
            self.ui.tableConstraints.setColumnCount(0)
            self.auto_save_schema = {
                'factor_options': [],
                'constraints': []
            }
            self.constraints_exist = False
            self.ui.buttonAdd.setEnabled(False)
            self.ui.buttonExcel.setEnabled(False)

    # method generates constraints for use in pairwise analysis. Didn't work when stored in helpers.py file
    def is_valid_combination(self, row):
        n = len(row)
        rows = len(self.processed_pairs) - 1
        if n > rows:
            con = helpers.get_constraints(self.auto_save_schema['constraints'])
            for i in con:
                if str(i[1]) == row[i[0]] and str(i[3]) == row[i[2]]:
                    return False
        return True

    def generate_analysis(self):
        # prepare factors/options for analysis
        self.processed_pairs = []
        for item in self.auto_save_schema['factor_options']:
            self.processed_pairs.append(item['options'])
        # work out total possible combinations
        fullcombinations = 1
        for i in range(0, len(self.processed_pairs)):
            fullcombinations *= len(self.processed_pairs[i])
        # perform analysis
        pairwise = None
        try:
            if len(self.auto_save_schema['factor_options']) > 1 and self.auto_save_schema['constraints']:
                pairwise = AllPairs(self.processed_pairs, filter_func=self.is_valid_combination)
            elif len(self.auto_save_schema['factor_options']) > 1:
                pairwise = AllPairs(self.processed_pairs)
            elif len(self.auto_save_schema['factor_options']) == 1:
                self.ui.labelMessage.setStyleSheet('color: red')
                self.ui.labelMessage.setText('Only one factor defined.  More than one is required to run pairwise analysis')
            else:
                self.ui.labelMessage.setStyleSheet('color: red')
                self.ui.labelMessage.setText('No options entered.  At least two factors with options must be defined')
        except Exception:
            self.ui.labelMessage.setStyleSheet('color: red')
            self.ui.labelMessage.setText('An error has occurred.  Check table contents for possible mistakes')
            raise
        if pairwise:
            # prepare output and read into array
            reduced = 0
            analysis_output = []
            for i, v in enumerate(pairwise):
                reduced += 1
                analysis_output.append(helpers.stringclean(str(v)))
            # insert combinations into results table
            self.ui.buttonExcel.setEnabled(True)
            resulttable = self.ui.tableResults
            resulttable.setColumnCount(0)
            resulttable.setRowCount(0)
            item = QtWidgets.QTableWidgetItem('Test Case')
            self.font.setBold(True)
            item.setFont(self.font)
            resulttable.insertColumn(0)
            resulttable.insertRow(0)
            resulttable.setItem(0, 0, item)
            for col, factor in enumerate(self.auto_save_schema['factor_options'], 1):
                item = QtWidgets.QTableWidgetItem(factor['factorName'])
                self.font.setBold(True)
                item.setFont(self.font)
                resulttable.insertColumn(col)
                resulttable.setItem(0, col, item)
            for row, combo in enumerate(analysis_output, 1):
                resulttable.insertRow(row)
                test_case_name = QtWidgets.QTableWidgetItem('tc-' + str(row))
                resulttable.setItem(row, 0, test_case_name)
                options = combo.replace('\n', '')
                options = options.split(',')
                for col, option in enumerate(options, 1):
                    item = QtWidgets.QTableWidgetItem(option)
                    resulttable.setItem(row, col, item)

            self.goto_results()
            self.ui.labelMessage.setStyleSheet('color: green')
            self.ui.labelMessage.setText('FINISHED! Reduced from ' + str(fullcombinations) + ' to ' +
                                         str(reduced) + ' combinations')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Main()
    myapp.show()
    sys.exit(app.exec_())
