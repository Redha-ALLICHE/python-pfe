from PyQt5 import QtCore, QtGui, QtWidgets
from gui.signinPage import Ui_SigninPage
import sys
from users.database import Database

class Ui_loginPage(QtWidgets.QDialog):
    """this class creates the login page"""
    def __init__(self):
        """create the login page object"""
        QtWidgets.QDialog.__init__(
            self, None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.setupUi(self)

    def checkCases(self):
        """checks if the inputs are empty """
        if not self.username_input.text():
            self.errorMsg("I think that you forget the username !")
        elif not self.password_input.text():
            self.errorMsg("I think that you forget the password !")
        else:
            self.goToMain()

    def goToMain(self):
        """check the login info and start the main page if they are true """
        entered_username = self.username_input.text()
        entered_password = self.password_input.text()
        db = Database()
        if db.checkLogin(entered_username,entered_password):
            print("go to the main")
            self.setRemember()
            db.closeDb()
        else:
            self.errorMsg("Incorrect username or password !")
            self.username_input.setText('')
            self.password_input.setText('')

    def goToSignin(self):
        """go to the signin page"""
        new_user = Ui_SigninPage()
        new_user.exec_()
        new_user.show()

    def errorMsg(self, msg):
        """display an error msg to the screen"""
        QtWidgets.QMessageBox.warning(
            self, "Login", msg, QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Ok)

    def setupUi(self, loginPage):
        """the login page setup ui"""
        loginPage.setWindowIcon(QtGui.QIcon("gui\\img\\logo.png"))
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
        self.rememberMe = QtWidgets.QCheckBox(loginPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rememberMe.sizePolicy().hasHeightForWidth())
        self.rememberMe.setSizePolicy(sizePolicy)
        self.rememberMe.setMaximumSize(QtCore.QSize(16777215, 50))
        self.rememberMe.setStyleSheet("QCheckBox{\n"
        "    font-size: 16px;\n"
        "    color: rgb(207, 210, 218);\n"
        "    margin: 10 0 0 10px;\n"
        "\n"
        "}")
        self.rememberMe.setObjectName("rememberMe")
        self.verticalLayout.addWidget(self.rememberMe, 0, QtCore.Qt.AlignVCenter)
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
        "    border: 1px solid transparent;\n"
        "    padding:5px 0;\n"
        "    border-color : rgb(25, 151, 198);\n"
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
        self.signin_btn.setObjectName("signin_btn")
        self.horizontalLayout.addWidget(self.signin_btn)
        self.login_btn = QtWidgets.QPushButton(loginPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setMinimumSize(QtCore.QSize(0, 10))
        self.login_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setStyleSheet("QPushButton{\n"
        "background-color: rgb(25, 151, 198);\n"
        "color: rgb(255, 255, 255);\n"
        "padding:8px 10px;\n"
        "border : 1px solid rgb(25, 151, 198);\n"
        "font-size:16px;\n"
        "font-weight:500;\n"
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
        self.login_btn.setAutoDefault(True)
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
        self.buttonLink()
        self.retranslateUi(loginPage)
        QtCore.QMetaObject.connectSlotsByName(loginPage)

    def buttonLink(self):
        """links the click events of the buttons"""
        self.login_btn.setAutoDefault(True)
        self.login_btn.clicked.connect(self.checkCases)
        self.signin_btn.clicked.connect(self.goToSignin)
        self.getRemember()
        self.signin_btn.setAutoDefault(False)

    def retranslateUi(self, loginPage):
        _translate = QtCore.QCoreApplication.translate
        loginPage.setWindowTitle(_translate("loginPage", "Login Page"))
        self.title.setText(_translate("loginPage", "Welcome to Network Automation"))
        self.username_input.setPlaceholderText(_translate("loginPage", "Username"))
        self.password_input.setPlaceholderText(_translate("loginPage", "Password"))
        self.rememberMe.setText(_translate("loginPage", "Remember me"))
        self.signin_btn.setText(_translate("loginPage", "Sign In"))
        self.login_btn.setText(_translate("loginPage", "Login"))
        self.label_2.setText(_translate("loginPage", "© 2018-2019"))

    def getRemember(self, path='gui/remember.txt'):
        """get the state of the remember"""
        with open(path) as f:
            data = f.readlines()
        if data:   
            if data[0].strip('\n') == "1":
                self.username_input.setText(data[1].strip('\n'))
                self.rememberMe.setChecked(True)

    def setRemember(self, path='gui/remember.txt'):
        """set the state of the remember"""
        with open(path, 'w') as f:
            if self.rememberMe.isChecked():
                f.write('1\n')
                f.write(self.username_input.text())
            else:
                f.write('0\n')
                f.write(' ')
                
