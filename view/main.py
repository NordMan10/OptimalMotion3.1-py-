import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
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

        self.initTable(self.output_data)
        self.fill_table(self.output_data)

    tableHeaders = ("Id ВС", "Тплан.", "Твозм.", "Тразр.", "Время обработки", "Необходимость обработки")

    # def keyPressEvent(self, e):
    #     if e.key() == QtCore.Qt.Key_F12:

    def initTable(self, output_data):
        self.ui.tableWidget.setGeometry(QtCore.QRect(100, 100, 1600, 800))

        self.ui.tableWidget.setRowCount(len(output_data))
        self.ui.tableWidget.setColumnCount(len(self.get_table_row_items(output_data[0])))
        # self.setTableHeaders()

    def fill_table(self, output_data):
        row = 0
        for table_row in output_data:
            col = 0
            output_members = self.get_table_row_items(table_row)

            for member in output_members:
                table_cell = QTableWidgetItem(member[1])

                # Только для чтения
                table_cell.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )

                self.ui.tableWidget.setItem(row, col, table_cell)
                col += 1

            row += 1

    def clear_table(self):
        self.ui.tableWidget.clear()

    def set_table_headers(self):
        self.ui.tableWidget.setHorizontalHeaderLabels(MyWindow.tableHeaders)

    def get_table_row_items(self, table_row):
        members = inspect.getmembers(table_row)
        result = []
        for member in members:
            if member[0].startswith("t"):
                result.append(member)

        return result

app = QtWidgets.QApplication([])
application = MyWindow()
application.show()


print("hello")



sys.exit(app.exec())
