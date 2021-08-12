import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QCheckBox, QHBoxLayout
from PyQt5.QtGui import QFont
from design import *
from Model import Model
from static.CommonInputData import CommonInputData
import inspect


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()

        self.model = Model(2, 2)

        self.unused_planned_moments = CommonInputData.input_taking_off_moments.get_unused_planned_moments()
        self.output_data = self.model.get_output_data(self.unused_planned_moments)

        self.init_table(self.output_data)
        self.fill_table(self.output_data)

        self.ui.tableWidget.resizeColumnsToContents()

    # def keyPressEvent(self, e):
    #     if e.key() == QtCore.Qt.Key_F12:

    def init_table(self, output_data):
        self.ui.tableWidget.setGeometry(QtCore.QRect(100, 100, 1600, 800))

        self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + len(output_data))
        self.ui.tableWidget.setColumnCount(self.ui.tableWidget.columnCount() + len(self.get_table_row_output_members(output_data[0])))

        self.ui.tableWidget.setFont(QFont("Roboto", 10))

        self.set_table_headers(self.get_table_row_output_members(output_data[0]))

    def set_table_headers(self, output_members):
        table_headers = self.get_output_data_headers(output_members)
        for i, header in enumerate(table_headers):
            header_item = QTableWidgetItem(header)
            header_item.setFont(QFont("Roboto", 10, QtGui.QFont.Bold))
            self.ui.tableWidget.setHorizontalHeaderItem(i, header_item)

    def fill_table(self, output_data):
        row = 0
        for table_row in output_data:
            output_members = self.get_table_row_output_members(table_row)
            output_values = self.get_output_data_values(output_members)
            col = 0

            for value in output_values:
                table_cell = QTableWidgetItem(value)

                if isinstance(value, bool):
                    check_box = MyWindow.create_checkbox_for_table(value)
                    self.ui.tableWidget.setCellWidget(row, col, check_box)
                else:
                    table_cell = QTableWidgetItem(value)

                    # Задаем режим только для чтения
                    table_cell.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                    )

                    self.ui.tableWidget.setItem(row, col, table_cell)
                col += 1

            row += 1

    def clear_table(self):
        self.ui.tableWidget.clear()

    def get_output_data_headers(self, output_members):
        return [item[1][0] for item in output_members]

    def get_output_data_values(self, output_members):
        return [item[1][1] for item in output_members]

    def get_table_row_output_members(self, table_row):
        members = inspect.getmembers(table_row)
        output_members = []
        for member in members:
            if member[0].startswith("t"):
                output_members.append(member)

        return output_members

    @staticmethod
    def create_checkbox_for_table(value):
        pWidget = QWidget()

        check_box = QCheckBox()
        if value:
            check_box.setCheckState(QtCore.Qt.Checked)
        else:
            check_box.setCheckState(QtCore.Qt.Unchecked)

        pLayout = QHBoxLayout(pWidget)
        pLayout.addWidget(check_box)
        pLayout.setAlignment(QtCore.Qt.AlignCenter)
        pLayout.setContentsMargins(0, 0, 0, 0)

        pWidget.setLayout(pLayout)
        return pWidget


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()


print("hello")

sys.exit(app.exec())
