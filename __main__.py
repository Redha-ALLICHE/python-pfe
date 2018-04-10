from gui.loginPage import Ui_loginPage
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        window = Ui_loginPage()
        window.show()
        sys.exit(app.exec_())
