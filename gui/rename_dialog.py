from PyQt5 import QtCore, QtGui, QtWidgets
from backend.telnet import TelnetDevice


class Rename_dialog(QtWidgets.QWidget):
    """the configure from script dialog window """
    request = QtCore.pyqtSignal(list)

    def __init__(self, ips):
        """create the backup dialog object"""
        self.ips = ips
        self.device = TelnetDevice()
        QtWidgets.QDialog.__init__(
            self, None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self._thread = QtCore.QThread()
        self.work = Threaded(text_signal=self.change_display,
                             label_signal=self.change_label, bar_signal=self.change_bar, done_signal=self._thread.quit)
        self.request.connect(self.work.automate_config)
        self._thread.started.connect(self.work.start)
        self._thread.finished.connect(self.after_work)
        self.work.moveToThread(self._thread)
        QtWidgets.qApp.aboutToQuit.connect(self._thread.quit)
        self.setupUi(self)

    def setupUi(self, rename_dialog):
            """the script dialog setup  """
        #main window
            rename_dialog.setObjectName("rename_dialog")
            rename_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
            rename_dialog.resize(543, 466)
        #main window vertical layout
            self.verticalLayout = QtWidgets.QVBoxLayout(rename_dialog)
            self.verticalLayout.setObjectName("verticalLayout")
        #toolbox container
            self.toolbox = QtWidgets.QWidget(rename_dialog)
            self.toolbox.setObjectName("toolbox")
        #toolbox horizontal layout
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.toolbox)
            self.horizontalLayout.setObjectName("horizontalLayout")
        #toolbox path input
            self.path_input = QtWidgets.QLineEdit(self.toolbox)
            self.path_input.setReadOnly(True)
            self.path_input.setObjectName("path_input")
            self.horizontalLayout.addWidget(self.path_input)
        #toolbox rename button
            self.rename_btn = QtWidgets.QPushButton(self.toolbox)
            self.rename_btn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.rename_btn.setObjectName("rename_btn")
            self.horizontalLayout.addWidget(self.rename_btn)
            self.rename_btn.clicked.connect(self.rename_script)
            self.verticalLayout.addWidget(self.toolbox)
        #loading label
            self.loading_label = QtWidgets.QLabel(rename_dialog)
            self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
            self.loading_label.setObjectName("loading_label")
            self.loading_label.hide()
            self.verticalLayout.addWidget(self.loading_label)
        #loading container
            self.loading_container = QtWidgets.QWidget(rename_dialog)
            self.loading_container.setObjectName("loading_container")
            self.verticalLayout.addWidget(self.loading_container)
            self.loading_container.hide()
        #loading hlayout
            self.loading_layout = QtWidgets.QHBoxLayout(self.loading_container)
            self.loading_layout.setObjectName("loading_layout")
        #loading bar
            self.loading_bar = QtWidgets.QProgressBar(self.loading_container)
            self.loading_bar.setProperty("value", 0)
            self.loading_bar.setMaximum(len(self.ips))
            self.loading_bar.setTextVisible(True)
            self.loading_bar.setTextDirection(
                QtWidgets.QProgressBar.TopToBottom)
            self.loading_bar.setFormat(" %p%")
            self.loading_bar.setObjectName("loading_bar")
            self.loading_bar.hide()
            self.loading_layout.addWidget(self.loading_bar)
        #Clear button
            self.clear_btn = QtWidgets.QPushButton(self.loading_container)
            self.clear_btn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.clear_btn.setObjectName("clear_btn")
            self.clear_btn.setText("Clear")
            self.clear_btn.hide()
            self.clear_btn.clicked.connect(self.reset_display)
            self.loading_layout.addWidget(self.clear_btn)
        #input login container
            self.login_container = QtWidgets.QWidget(rename_dialog)
            self.login_container.setObjectName("login_container")
            self.verticalLayout.addWidget(self.login_container)
            self.login_container.hide()
        #input login horizontal layout
            self.login_layout = QtWidgets.QHBoxLayout(self.login_container)
            self.login_layout.setObjectName("login_layout")
            self.login_layout.setContentsMargins(0, 0, 0, 0)
        #input login username input
            self.login_username = QtWidgets.QLineEdit(self.login_container)
            self.login_username.setObjectName("login_username")
            self.login_username.setPlaceholderText("Username")
            self.login_layout.addWidget(self.login_username)
        #input login password input
            self.login_password = QtWidgets.QLineEdit(self.login_container)
            self.login_password.setObjectName("login_password")
            self.login_password.setPlaceholderText("Password")
            self.login_password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.login_layout.addWidget(self.login_password)
        #input login secret input
            self.login_secret = QtWidgets.QLineEdit(self.login_container)
            self.login_secret.setObjectName("login_secret")
            self.login_secret.setPlaceholderText("Privilege Password")
            self.login_layout.addWidget(self.login_secret)
            self.login_secret.setEchoMode(QtWidgets.QLineEdit.Password)
        #input login button
            self.login_button = QtWidgets.QPushButton(self.login_container)
            self.login_button.setObjectName("login_button")
            self.login_button.setText("Confirm")
            self.login_button.clicked.connect(self.toogle)
            self.login_layout.addWidget(self.login_button)
        #display text widget
            self.display_text = QtWidgets.QTextEdit(rename_dialog)
            self.display_text.setObjectName("display_text")
            self.display_text.setReadOnly(False)
            self.display_text.setPlaceholderText(
                "The new name for  : " + '\nThe new name for : '.join(self.ips))
            self.verticalLayout.addWidget(self.display_text)

            self.retranslateUi(rename_dialog)
            QtCore.QMetaObject.connectSlotsByName(rename_dialog)

    def retranslateUi(self, rename_dialog):
        _translate = QtCore.QCoreApplication.translate
        rename_dialog.setWindowTitle(_translate(
            "rename_dialog", "Apply configuration from script"))
        self.rename_btn.setText(_translate("rename_dialog", "Rename"))
        self.path_input.setPlaceholderText(
            _translate("rename_dialog", "Please input the new names down below"))
        self.loading_label.setText(_translate(
            "rename_dialog", "Executing the script"))

    def rename_script(self):
        """action when the apply button is pressed"""
        self.name_list = self.display_text.toPlainText().split('\n')
        if len(self.name_list) == len(self.ips):
            self.display_text.clear()
            self.path_input.clear()
            self.loading_label.show()
            self.loading_bar.setValue(0)
            self.toolbox.setEnabled(False)
            self.display_text.setReadOnly(True)
            self.loading_label.setText("Working on :" + self.ips[0])
            self.loading_container.show()
            self.loading_bar.show()
            self._thread.start()
            self.request.emit([self.ips, self.name_list, self.getInputs])
        else:
            self.path_input.setText(
                "Please input " + str(len(self.ips))+" names ")

    def getInputs(self, data, mode="check"):
        """input the login info"""
        self.loop = True
        if mode == "ask":
            self.login_container.show()
            while self.loop:
                self.loading_label.setText(
                    "Input the login for : " + data["ip"])
                QtCore.QCoreApplication.processEvents()
            data["userame"] = self.login_username.text()
            data["password"] = self.login_password.text()
            data["secret"] = self.login_secret.text()

        elif mode == "privilegeOnly":
            self.login_container.show()
            self.login_username.hide()
            self.login_password.hide()
            while self.loop:
                self.loading_label.setText(
                    "Input the privilege password for the ip =  " + data["ip"])
                QtCore.QCoreApplication.processEvents()
            data["secret"] = self.login_secret.text()

        elif mode == "check":
            index = self.device.myDb.searchDevice(data)
            if index != "EOL" and self.device.myDb.all_info[index]["username"] and self.device.myDb.all_info[index]["password"]:
                if self.device.myDb.all_info[index]["secret"] == '':
                    self.getInputs(data, mode='privilegeOnly')
                data = self.device.myDb.all_info[index].copy()
        self.reset_view()
        return data

    def toogle(self):
        """when confirm button is pressed"""
        self.loop = False

    def reset_view(self):
        """when the inputs are done"""
        self.login_username.clear()
        self.login_username.show()
        self.login_password.clear()
        self.login_password.show()
        self.login_secret.clear()
        self.login_secret.show()
        self.login_container.hide()

    @QtCore.pyqtSlot(str)
    def change_display(self, text):
        """changes the text in the display text"""
        self.display_text.insertPlainText(text)

    @QtCore.pyqtSlot(int)
    def change_bar(self, num):
        """changes the text in the display text"""
        self.loading_bar.setValue(num)

    @QtCore.pyqtSlot(str)
    def change_label(self, text):
        """changes the text in the display text"""
        self.loading_label.setText(text)

    @QtCore.pyqtSlot()
    def reset_display(self):
        """changes the text in the display text"""
        self.toolbox.setEnabled(True)
        self.loading_bar.setValue(0)
        self.loading_bar.hide()
        self.display_text.clear()
        self.login_container.hide()
        self.loading_label.hide()
        self.clear_btn.hide()
        self.loading_container.hide()

    @QtCore.pyqtSlot()
    def after_work(self):
        self.clear_btn.show()
        self.loading_label.setText("Working done")


class Threaded(QtCore.QObject):
    text_signal = QtCore.pyqtSignal(str)
    bar_signal = QtCore.pyqtSignal(int)
    label_signal = QtCore.pyqtSignal(str)
    done_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.device = TelnetDevice()
        self.done_signal.connect(self.exit_process)

    @QtCore.pyqtSlot()
    def start(self): print("Thread started")

    @QtCore.pyqtSlot(list)
    def automate_config(self, args):
        """         self.ips, name_list, funct = self.getInputs """
        increment = [self.bar_signal, self.label_signal,
                     self.text_signal, self.done_signal]
        self.device.rename(args[0], args[1], args[2], increment)

    @QtCore.pyqtSlot()
    def exit_process(self):
        print("Thread stopped")
        self.device.exit_process()
