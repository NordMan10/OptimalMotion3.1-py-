import sys
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QCheckBox, QHBoxLayout
from PyQt5.QtGui import QFont
from design import *
from Model import Model
from static.CommonInputData import CommonInputData
import inspect


class MyWindow(QtWidgets.QMainWindow):
    """Главное окно проекта"""

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()

        self.model = Model(2, 2)

        self.unused_planned_moments = CommonInputData.input_taking_off_moments.get_unused_planned_moments()
        self.output_data = self.model.get_output_data(self.unused_planned_moments)

        self.init_table(self.output_data)

        self.init_buttons()

        self.ui.tableWidget.resizeColumnsToContents()

    def fill_table_by_taking_off_aircrafts_data(self):
        """
        Получает список выходных данных и заполняет ими таблицу
        """

        self.unused_planned_moments = CommonInputData.input_taking_off_moments.get_unused_planned_moments()
        self.output_data = self.model.get_output_data(self.unused_planned_moments)

        self.set_table_headers(self.get_table_row_output_members(self.output_data[0]))
        self.fill_table(self.output_data)

    # <editor-fold desc="Table Methods">

    def init_table(self, output_data):
        """Инициализация Таблицы"""

        self.ui.tableWidget.setGeometry(QtCore.QRect(100, 100, 1600, 800))

        self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + len(output_data))
        self.ui.tableWidget.setColumnCount(self.ui.tableWidget.columnCount() + len(self.get_table_row_output_members(output_data[0])))

        self.ui.tableWidget.setFont(QFont("Roboto", 10))

        self.set_table_headers(self.get_table_row_output_members(self.output_data[0]))

    def set_table_headers(self, output_members):
        """Задает заголовки таблицы"""

        table_headers = self.get_output_data_headers(output_members)
        for i, header in enumerate(table_headers):
            header_item = QTableWidgetItem(header)
            header_item.setFont(QFont("Roboto", 10, QtGui.QFont.Bold))
            self.ui.tableWidget.setHorizontalHeaderItem(i, header_item)

    def fill_table(self, output_data):
        """Заполнят таблицу предоставленными данными"""

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

    def get_output_data_headers(self, output_members):
        """Возвращает список значений для заголовков таблицы"""

        return [item[1][0] for item in output_members]

    def get_output_data_values(self, output_members):
        """Возвращает список значений для строки таблицы"""

        return [item[1][1] for item in output_members]

    def get_table_row_output_members(self, table_row):
        """Возвращает список аттрибутов класса TableRow"""

        members = inspect.getmembers(table_row)
        output_members = []
        for member in members:
            if member[0].startswith("t"):
                output_members.append(member)

        return output_members

    @staticmethod
    def create_checkbox_for_table(value):
        """Создает и возвращает QtCheckBox для таблицы"""

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
    # </editor-fold>

    # <editor-fold desc="Buttons Methods">
    def init_buttons(self):
        """Инициализация всех кнопок"""

        self.init_start_button()
        self.init_reset_button()

    def init_start_button(self):
        self.ui.start_button.clicked.connect(self.start_button_click_handler)
        self.ui.start_button.setGeometry(100, 30, 100, 40)
        self.ui.start_button.setText("Старт")
        self.ui.start_button.setFont(QFont("Roboto", 11, QFont.Bold))

    def init_reset_button(self):
        self.ui.reset_button.clicked.connect(self.reset_button_click_handler)
        self.ui.reset_button.setGeometry(300, 30, 200, 40)
        self.ui.reset_button.setText("Очистить таблицу")
        self.ui.reset_button.setFont(QFont("Roboto", 11, QFont.Bold))

    def start_button_click_handler(self):
        self.fill_table_by_taking_off_aircrafts_data()

    def reset_button_click_handler(self):
        self.ui.tableWidget.clear()

        CommonInputData.input_taking_off_moments.reset_last_planned_taking_off_moment_index()
        CommonInputData.input_taking_off_moments.reset_last_permitted_taking_off_moment_index()

        self.model.reset_runways()
        self.model.reset_special_places()

        self.set_table_headers(self.get_table_row_output_members(self.output_data[0]))
        self.output_data.clear()

    # </editor-fold>


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
