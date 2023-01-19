
from PyQt5 import QtWidgets

from MainPage import Ui_MainPage
from display import Ui_Display


class first_window(QtWidgets.QMainWindow, Ui_MainPage):
    def __int__(self, parent=None):
        super(first_window, self).__int__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hide)


class second_window(QtWidgets.QDialog, Ui_Display):
    def __int__(self, parent=None):
        super(second_window, self).__int__(parent)
        self.setupUi(self)
        self.BackButton.clicked.connect(self.hide)


class manager:
    def __int__(self):
        self.first = first_window()
        self.second = second_window()

        self.first.pushButton.clicked.connect(self.second.show)
        self.second.BackButton.clicked.connect(self.first.show)

        self.first.show()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    manager = manager()
    sys.exit(app.exec_())

