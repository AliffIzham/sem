from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets


class first_window(QWidget):
    def __int__(self):
        super(first_window, self).__init__()
        loadUi("MainPage.ui", self)

    def openDisplay(self):
        display = second_window()
        widget.addWidget(display)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class second_window(QWidget):
    def __int__(self):
        super(second_window, self).__int__()
        loadUi("Display.ui", self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    widget = first_window()
    #widget.addWidget(mainPage)
    widget.show()

    #ui = Ui_MainPage()
    #ui.setupUi(MainPage)
    #window.show()
    sys.exit(app.exec_())
