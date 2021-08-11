import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from myDesign import *
from Model import Model
from static.CommonInputData import CommonInputData


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = MyWindow()
# application.show()


print("hello")

model = Model(2, 2)

unused_planned_moments = CommonInputData.input_taking_off_moments.get_unused_planned_moments()
model.get_output_data(unused_planned_moments)

sys.exit(app.exec())
