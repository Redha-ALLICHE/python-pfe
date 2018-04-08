# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_loginPage(object):

    def setupUi(self, loginPage):
        """the login page setup ui"""
        loginPage.setWindowIcon(QtGui.QIcon("gui\\logo.png"))
        loginPage.setObjectName("loginPage")
        loginPage.resize(430, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginPage.sizePolicy().hasHeightForWidth())
        loginPage.setSizePolicy(sizePolicy)
        loginPage.setMinimumSize(QtCore.QSize(430, 480))
        loginPage.setMaximumSize(QtCore.QSize(430, 480))
        loginPage.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        loginPage.setAutoFillBackground(False)
        loginPage.setStyleSheet(
        "background-color: rgb(37, 40, 48);\n"
        "color: rgb(207, 210, 218);\n"
        "")
        self.verticalLayout = QtWidgets.QVBoxLayout(loginPage)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.title = QtWidgets.QLabel(loginPage)
        self.title.setMinimumSize(QtCore.QSize(400, 20))
        self.title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setStyleSheet("QLabel{\n"
        "    font: 15pt \"Arial\";\n"
        "    color: rgb(25, 151, 198);    \n"
        "    padding :10px;\n"
        "\n"
        "}\n"
        "")
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setScaledContents(True)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(False)
        self.title.setIndent(-1)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.username_input = QtWidgets.QLineEdit(loginPage)
        self.username_input.setStyleSheet("QLineEdit{\n"
        "    background-color: rgb(255, 255, 255,0);\n"
        "    color: rgb(207, 210, 218);\n"
        "    padding: 10px;\n"
        "    font-size: 16px;\n"
        "    border:none;\n"
        "\n"
        "}\n"
        "")
        self.username_input.setObjectName("username_input")
        self.verticalLayout.addWidget(self.username_input)
        self.line = QtWidgets.QFrame(loginPage)
        self.line.setStyleSheet(
        "    background-color: rgb(15, 141, 188);\n"
        "    margin:0 10px 0 10px;\n")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.password_input = QtWidgets.QLineEdit(loginPage)
        self.password_input.setStyleSheet("QLineEdit{\n"
        "    background-color: rgb(255, 255, 255,0);\n"
        "    color: rgb(207, 210, 218);\n"
        "    padding: 10px;\n"
        "    font-size: 16px;\n"
        "    border:none;\n"
        "\n"
        "}")
        self.password_input.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.verticalLayout.addWidget(self.password_input)
        self.line_2 = QtWidgets.QFrame(loginPage)
        self.line_2.setStyleSheet(
        "    background-color: rgb(15, 141, 188);\n"
        "    margin:0 10px 0 10px;\n")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.rememberme_check = QtWidgets.QCheckBox(loginPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rememberme_check.sizePolicy().hasHeightForWidth())
        self.rememberme_check.setSizePolicy(sizePolicy)
        self.rememberme_check.setMaximumSize(QtCore.QSize(16777215, 50))
        self.rememberme_check.setStyleSheet("QCheckBox{\n"
        "    font-size: 16px;\n"
        "    color: rgb(207, 210, 218);\n"
        "    margin: 10 0 0 10px;\n"
        "\n"
        "}")
        self.rememberme_check.setObjectName("rememberme_check")
        self.verticalLayout.addWidget(self.rememberme_check, 0, QtCore.Qt.AlignVCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.signin_btn = QtWidgets.QPushButton(loginPage)
        self.signin_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.signin_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signin_btn.setStyleSheet("QPushButton{\n"
        "    \n"
        "    background-color: rgba(240, 240, 240, 0);\n"
        "    color: rgb(25, 151, 198);    \n"
        "    border: 3px solid transparent;\n"
        "    border-color: rgb(25, 151, 198);\n"
        "    font-size:16px;\n"
        "    border-radius: 10px;\n"
        "\n"
        "}\n"
        "QPushButton:hover{\n"
        "\n"
        "    color: rgb(255, 255, 255);\n"
        "    background-color: rgb(25, 151, 198);\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(0, 111, 158);\n"
        "    border-color: rgb(0, 111, 158);\n"
        "}\n"
        "\n"
        "\n"
        "")
        self.signin_btn.setInputMethodHints(QtCore.Qt.ImhNone)
        self.signin_btn.setObjectName("signin_btn")
        self.horizontalLayout.addWidget(self.signin_btn)
        self.login_btn = QtWidgets.QPushButton(loginPage)
        self.login_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 10))
        self.login_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setMouseTracking(True)
        self.login_btn.setTabletTracking(False)
        self.login_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.login_btn.setStyleSheet("QPushButton{\n"
        "background-color: rgb(25, 151, 198);\n"
        "color: rgb(255, 255, 255);\n"
        "padding-right: 10px;\n"
        "padding-left: 10px;\n"
        "font-size:16px;\n"
        "border-radius: 10px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(5, 131, 178);\n"
        "}\n"
        "QPushButton:pressed{\n"
        "background-color: rgb(0, 111, 158);\n"
        "}\n"
        "\n"
        "\n"
        "")
        self.login_btn.setAutoRepeatDelay(100)
        self.login_btn.setAutoDefault(False)
        self.login_btn.setDefault(False)
        self.login_btn.setFlat(False)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout.addWidget(self.login_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(loginPage)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setStyleSheet("font-size: 10px;\n"
        "color: rgb(108, 117, 125);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.title.setBuddy(self.title)
        self.login_btn.clicked.connect(self.goToMain)
        self.signin_btn.clicked.connect(self.goToSignin)

        self.retranslateUi(loginPage)
        QtCore.QMetaObject.connectSlotsByName(loginPage)

    def goToMain(self):
        pass

    def goToSignin(self):
        pass

    def retranslateUi(self, loginPage):
        _translate = QtCore.QCoreApplication.translate
        loginPage.setWindowTitle(_translate("loginPage", "Login Page"))
        self.title.setText(_translate("loginPage", "Welcome to Network Automation"))
        self.username_input.setPlaceholderText(_translate("loginPage", "Username"))
        self.password_input.setPlaceholderText(_translate("loginPage", "Password"))
        self.rememberme_check.setText(_translate("loginPage", "Remember me"))
        self.signin_btn.setText(_translate("loginPage", "Sign In"))
        self.login_btn.setText(_translate("loginPage", "Login"))
        self.label_2.setText(_translate("loginPage", "© 2018-2019"))

if __name__=='__main__':
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QWidget()
        ui =Ui_loginPage()
        ui.setupUi(window)
        window.show()
        sys.exit(app.exec_())