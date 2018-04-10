from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from users.database import Database

class Ui_SigninPage(QtWidgets.QDialog):
    """this class creates and shows the signIn page"""

    def __init__(self):
        QtWidgets.QDialog.__init__(self, None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.setupUi(self)
        
    def setupUi(self, SigninPage):
        SigninPage.setObjectName("SigninPage")
        SigninPage.resize(430, 480)
        SigninPage.setWindowModality(QtCore.Qt.ApplicationModal)
        SigninPage.setMaximumSize(QtCore.QSize(430, 480))
        SigninPage.setStyleSheet("background-color: rgb(37, 40, 48);\n"
        "color: rgb(207, 210, 218);\n"
        "")
        self.gridLayout = QtWidgets.QGridLayout(SigninPage)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLabel(SigninPage)
        self.title.setMinimumSize(QtCore.QSize(400, 50))
        self.title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setStyleSheet("QLabel{\n"
        "    font: 19pt \"Arial\";\n"
        "    color: rgb(25, 151, 198);    \n"
        "    padding :10px;\n"
        "\n"
        "\n"
        "}\n"
        "")
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setScaledContents(True)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(False)
        self.title.setIndent(-1)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 0, 1, 1)
        self.username_input = QtWidgets.QLineEdit(SigninPage)
        self.username_input.setToolTip("")
        self.username_input.setStyleSheet("QLineEdit{\n"
        "    background-color: rgb(255, 255, 255,0);\n"
        "    color: rgb(207, 210, 218);\n"
        "    padding: 10px;\n"
        "    font-size: 16px;\n"
        "    border:none;\n"
        "\n"
        "}\n"
        "")
        self.username_input.setText("")
        self.username_input.setObjectName("username_input")
        self.gridLayout.addWidget(self.username_input, 3, 0, 1, 1)
        self.confirm_password = QtWidgets.QLineEdit(SigninPage)
        self.confirm_password.setStyleSheet("QLineEdit{\n"
        "    background-color: rgb(255, 255, 255,0);\n"
        "    color: rgb(207, 210, 218);\n"
        "    padding: 10px;\n"
        "    font-size: 16px;\n"
        "    border:none;\n"
        "\n"
        "}")
        self.confirm_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password.setObjectName("confirm_password")
        self.gridLayout.addWidget(self.confirm_password, 9, 0, 1, 1)
        self.submit_btn = QtWidgets.QPushButton(SigninPage)
        self.submit_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.submit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_btn.setStyleSheet("QPushButton{\n"
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
        self.submit_btn.setInputMethodHints(QtCore.Qt.ImhNone)
        self.submit_btn.setObjectName("submit_btn")
        self.gridLayout.addWidget(self.submit_btn, 13, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(SigninPage)
        self.line_3.setStyleSheet(
        "    background-color: rgb(15, 141, 188);\n"
        "    margin:0 10px 0 10px;\n")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 8, 0, 1, 1)
        self.line = QtWidgets.QFrame(SigninPage)
        self.line.setStyleSheet(
        "    background-color: rgb(15, 141, 188);\n"
        "    margin:0 10px 0 10px;\n")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 1)
        self.password_input = QtWidgets.QLineEdit(SigninPage)
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
        self.gridLayout.addWidget(self.password_input, 7, 0, 1, 1)
        self.copyright = QtWidgets.QLabel(SigninPage)
        self.copyright.setMaximumSize(QtCore.QSize(16777215, 20))
        self.copyright.setStyleSheet("font-size: 10px;\n"
        "color: rgb(108, 117, 125);")
        self.copyright.setObjectName("copyright")
        self.gridLayout.addWidget(self.copyright, 15, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.line_4 = QtWidgets.QFrame(SigninPage)
        self.line_4.setStyleSheet(
        "    background-color: rgb(15, 141, 188);\n"
        "    margin:0 10px 0 10px;\n")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 10, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(SigninPage)
        self.line_2.setStyleSheet(
        "    background-color: rgb(15, 141, 188);\n"
        "    margin:0 10px 0 10px;\n")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 6, 0, 1, 1)
        self.email_input = QtWidgets.QLineEdit(SigninPage)
        self.email_input.setStyleSheet("QLineEdit{\n"
        "    background-color: rgb(255, 255, 255,0);\n"
        "    color: rgb(207, 210, 218);\n"
        "    padding: 10px;\n"
        "    font-size: 16px;\n"
        "    border:none;\n"
        "}")
        self.email_input.setInputMethodHints(QtCore.Qt.ImhNone)
        self.email_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.email_input.setObjectName("email_input")
        self.gridLayout.addWidget(self.email_input, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 14, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 11, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.title.setBuddy(self.title)
        self.submit_btn.clicked.connect(self.validateInfo)
        self.retranslateUi(SigninPage)
        QtCore.QMetaObject.connectSlotsByName(SigninPage)

    def retranslateUi(self, SigninPage):
        _translate = QtCore.QCoreApplication.translate
        SigninPage.setWindowTitle(_translate("SigninPage", "Sign In"))
        self.title.setText(_translate("SigninPage", "Sign In"))
        self.username_input.setPlaceholderText(_translate("SigninPage", "Username"))
        self.confirm_password.setPlaceholderText(_translate("SigninPage", "Confirm Password"))
        self.submit_btn.setText(_translate("SigninPage", "Submit"))
        self.password_input.setPlaceholderText(_translate("SigninPage", "Password"))
        self.copyright.setText(_translate("SigninPage", "© 2018-2019"))
        self.email_input.setPlaceholderText(_translate("SigninPage", "Email"))
    
    def errorMsg(self, msg):
        """display an error msg to the screen"""
        QtWidgets.QMessageBox.warning(
            self, "Login", msg, QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Ok)

    def validateInfo(self):
        """validate the inputs from the users"""
        user = self.username_input.text()
        passw = self.password_input.text()
        confirm = self.confirm_password.text()
        mail = self.email_input.text()
        if not user :
            self.errorMsg("You forget to enter the username")
        elif not passw:
            self.errorMsg("You forget to enter the password")
        elif not confirm:
            self.errorMsg("You forget to enter the confirmation of the password")
        elif passw != confirm:
            self.errorMsg("the confirmation password is not the same as the password")
        elif not mail:
            self.errorMsg("You forget to enter the email")
        else:
            self.addUser(user, passw, mail)

    def addUser(self , user, passw, mail):
        """adds a new user to the database"""
        db = Database()
        if db.addUser(user, passw, mail):
            QtWidgets.QMessageBox.information(self,"Sign In","the new user is added",QtWidgets.QMessageBox.Ok)
            db.save()
            db.closeDb()
            self.close()
        else:
            self.errorMsg("Failed to add a new user verify your inputs")
