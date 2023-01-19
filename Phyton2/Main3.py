from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from MainPage import Ui_MainPage
from display import Ui_Display


class first_window(QWidget, Ui_MainPage):
    def __int__(self):
        super(first_window, self).__init__()
        self.setupUi(self)
        #self.show()
        self.pushButton.clicked.connect(self.openDisplay)

    def openDisplay(self):
        self.form = second_window()
        self.form.setupUi(self.open)
        self.form.show()
        first_window.hide()


class second_window(QWidget, Ui_Display):
    def __int__(self):
        super(second_window(), self).__init__()
        self.setupUi(self)
        #self.show()

    def openMainpage(self):
        self.form = first_window()
        self.form.setupUi(self.open)
        self.form.show()
        second_window.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = first_window()
    mainwindow.show()
    sys.exit(app.exec_())