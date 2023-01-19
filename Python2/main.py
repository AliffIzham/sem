import sys

from PyQt5.QtWidgets import *

from MainPage import Ui_MainPage
from Display import Ui_Display


class first_window(QWidget, Ui_MainPage):
    
    def __int__(self):
        super(first_window, self).__int__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.gotosecond)

    def gotosecond(self):
        this = second_window()
        this.show()
        self.hide()


class second_window(QWidget, Ui_Display):

    def __int__(self):
        super(second_window, self).__int__()
        self.setupUi(self)
        self.BackButton.clicked.connect(self.gotofirst)

    def gotofirst(self):
        that = first_window()
        that.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication([])
    window = first_window()
    window.show()
    sys.exit(app.exec_())
