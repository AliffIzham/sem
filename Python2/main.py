from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from Database import *
from Display import Ui_Display
from MainPage import Ui_MainPage


class first_window(QWidget, Ui_MainPage):
    
    def __init__(self):
        super(first_window, self).__init__()
        self.setupUi(self)
        self.this = second_window()
        self.pushButton.clicked.connect(self.gotosecond)

    def gotosecond(self):
        self.trackingnum = self.track_ID.text()
        if(check(self.trackingnum)):
            self.this.textBrowser.setText(self.trackingnum)
            self.this.textBrowser.setAlignment(QtCore.Qt.AlignCenter)
        else:
            self.this.textBrowser.setText("INVALID")
            self.this.textBrowser.setAlignment(QtCore.Qt.AlignCenter)

        self.this.textBrowser_2.setText(show_one_display(self.trackingnum, 1))
        self.this.textBrowser_2.setAlignment(QtCore.Qt.AlignCenter)
        self.this.textBrowser_3.setText(show_one_display(self.trackingnum, 2))
        self.this.textBrowser_3.setAlignment(QtCore.Qt.AlignCenter)
        self.this.textBrowser_4.setText(show_one_display(self.trackingnum, 3))
        self.this.textBrowser_4.setAlignment(QtCore.Qt.AlignCenter)
        self.this.show()
        self.hide()


class second_window(QWidget, Ui_Display):

    def __init__(self):
        super(second_window, self).__init__()
        self.setupUi(self)
        #self.that = first_window()
        self.BackButton.clicked.connect(self.hide)


"""    def gotofirst(self):
        self.that.show()
        self.hide()
"""

if __name__ == '__main__':
    app = QApplication([])
    window = first_window()
    window.show()
    app.exec_()
