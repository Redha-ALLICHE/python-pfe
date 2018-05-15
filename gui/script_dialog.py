from PyQt5 import QtCore, QtGui, QtWidgets
from backend.telnet import TelnetDevice


class Script_dialog(QtWidgets.QWidget):
    """the configure from script dialog window """
    request = QtCore.pyqtSignal(list)

    def __init__(self, ips):
        """create the script dialog object"""
        self.ips = ips
        self.commands = []
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

    def setupUi(self, script_dialog):
            """the script dialog setup  """
        #main window
            script_dialog.setObjectName("script_dialog")
            script_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
            script_dialog.resize(543, 466)
        #main window vertical layout
            self.verticalLayout = QtWidgets.QVBoxLayout(script_dialog)
            self.verticalLayout.setObjectName("verticalLayout")
        #toolbox container
            self.toolbox = QtWidgets.QWidget(script_dialog)
            self.toolbox.setObjectName("toolbox")
        #toolbox horizontal layout
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.toolbox)
            self.horizontalLayout.setObjectName("horizontalLayout")
        #toolbox path input
            self.path_input = QtWidgets.QLineEdit(self.toolbox)
            self.path_input.setReadOnly(True)
            self.path_input.setObjectName("path_input")
            self.horizontalLayout.addWidget(self.path_input)
        #toolbox open button
            self.open_btn = QtWidgets.QPushButton(self.toolbox)
            self.open_btn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.open_btn.setObjectName("open_btn")
            self.horizontalLayout.addWidget(self.open_btn)
            self.open_btn.setAutoDefault(True)
            self.open_btn.clicked.connect(self.open_file)
        #toolbox reset button
            self.reset_btn = QtWidgets.QPushButton(self.toolbox)
            self.reset_btn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.reset_btn.setObjectName("reset_btn")
            self.horizontalLayout.addWidget(self.reset_btn)
            self.reset_btn.clicked.connect(self.clear_display)
        #toolbox apply button
            self.apply_btn = QtWidgets.QPushButton(self.toolbox)
            self.apply_btn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.apply_btn.setObjectName("apply_btn")
            self.horizontalLayout.addWidget(self.apply_btn)
            self.apply_btn.clicked.connect(self.apply_script)
            self.verticalLayout.addWidget(self.toolbox)
        #checkboxes bar container
            self.container = QtWidgets.QWidget(script_dialog)
            self.container.setObjectName("container")
            self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.container)
            #self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
        #checkboxes widget container
            self.widget = QtWidgets.QWidget(self.container)
            self.widget.setObjectName("widget")
        #checkboxes horizontal layout
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
            self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_2.setSpacing(6)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #checkboxes select mode combobox
            self.select_mode = QtWidgets.QComboBox(self.widget)
            self.select_mode.addItem("Check login from the db")
            self.select_mode.addItem("One login for all")
            self.select_mode.addItem("Ask for login")
            self.select_mode.setObjectName("select_mode")
            self.horizontalLayout_2.addWidget(self.select_mode)
        #checkboxes privilege checkbox
            self.privilege_check = QtWidgets.QCheckBox(self.widget)
            self.privilege_check.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.privilege_check.setObjectName("privilege_check")
            self.horizontalLayout_2.addWidget(self.privilege_check)
        #checkboxes add checkbox
            self.add_check = QtWidgets.QCheckBox(self.widget)
            self.add_check.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.add_check.setObjectName("add_check")
            self.horizontalLayout_2.addWidget(self.add_check)
        #checkboxes silent checkbox
            self.silent_check = QtWidgets.QCheckBox(self.widget)
            self.silent_check.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.silent_check.setObjectName("silent_check")
            self.horizontalLayout_2.addWidget(self.silent_check)
        #checkbox backup checkbox
            self.backup_check = QtWidgets.QCheckBox(self.widget)
            self.backup_check.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.backup_check.setObjectName("backup_check")
            self.horizontalLayout_2.addWidget(self.backup_check)
            self.backup_check.toggled.connect(self.backupPath_show)
        #checkboxes backup path container
            self.backup_path_container = QtWidgets.QWidget(self.widget)
            self.backup_path_container.setObjectName("backup_path_container")
            self.backup_path_container.hide()
        #checkboxes backup path horizontal layout
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(
                self.backup_path_container)
            #self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_3.setSpacing(3)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        #checkboxes backup path input
            self.backup_path_input = QtWidgets.QLineEdit(
                self.backup_path_container)
            self.backup_path_input.setEnabled(True)
            self.backup_path_input.setObjectName("backup_path_input")
            self.backup_path_input.setText("backups")
            self.horizontalLayout_3.addWidget(self.backup_path_input)
        #checkboxes backup path change button
            self.change_path_btn = QtWidgets.QToolButton(
                self.backup_path_container)
            self.change_path_btn.setObjectName("change_path_btn")
            self.horizontalLayout_3.addWidget(self.change_path_btn)
            self.horizontalLayout_2.addWidget(self.backup_path_container)
            self.verticalLayout_2.addWidget(self.widget)
            self.change_path_btn.clicked.connect(self.change_backup_path)
            self.verticalLayout.addWidget(self.container)
        #loading label
            self.loading_label = QtWidgets.QLabel(script_dialog)
            self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
            self.loading_label.setObjectName("loading_label")
            self.loading_label.hide()
            self.verticalLayout.addWidget(self.loading_label)
        #loading container
            self.loading_container = QtWidgets.QWidget(script_dialog)
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
        #cancel button
            self.retry_btn = QtWidgets.QPushButton(self.loading_container)
            self.retry_btn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.retry_btn.setObjectName("retry_btn")
            self.retry_btn.setText("Clear")
            self.retry_btn.hide()
            self.retry_btn.clicked.connect(self.reset_display)
            self.loading_layout.addWidget(self.retry_btn)
        #input login container
            self.login_container = QtWidgets.QWidget(script_dialog)
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
            self.login_secret.hide()
        #input login button
            self.login_button = QtWidgets.QPushButton(self.login_container)
            self.login_button.setObjectName("login_button")
            self.login_button.setText("Confirm")
            self.login_button.clicked.connect(self.toogle)
            self.login_layout.addWidget(self.login_button)
        #display text widget
            self.display_text = QtWidgets.QTextEdit(script_dialog)
            self.display_text.setObjectName("display_text")
            self.verticalLayout.addWidget(self.display_text)

            self.retranslateUi(script_dialog)
            QtCore.QMetaObject.connectSlotsByName(script_dialog)

    def retranslateUi(self, script_dialog):
        _translate = QtCore.QCoreApplication.translate
        script_dialog.setWindowTitle(_translate(
            "script_dialog", "Apply configuration from script"))
        self.open_btn.setText(_translate("script_dialog", "Open"))
        self.reset_btn.setText(_translate("script_dialog", "Reset"))
        self.apply_btn.setText(_translate("script_dialog", "Apply"))
        self.path_input.setPlaceholderText(
            _translate("script_dialog", "Press open to select a file -->"))
        self.privilege_check.setText(_translate("script_dialog", "Privilege"))
        self.add_check.setText(_translate("script_dialog", "Add to database"))
        self.silent_check.setText(_translate("script_dialog", "Silent"))
        self.backup_check.setText(_translate("script_dialog", "Backup"))
        self.backup_path_input.setPlaceholderText(
            _translate("script_dialog", "Backup path"))
        self.change_path_btn.setText(_translate("script_dialog", "..."))
        self.loading_label.setText(_translate(
            "script_dialog", "Executing the script"))

    def open_file(self):
        """action when toolbox open button is pressed"""
        path = QtWidgets.QFileDialog.getOpenFileName(self, QtCore.QCoreApplication.translate(
            "script_dialog", "Choose the script text file "), "backend/", QtCore.QCoreApplication.translate("script_dialog", "Text File(*.txt)"))[0]
        self.path_input.setText(path)
        try:
            with open(path, 'r') as f:
                text = ''.join(f.readlines())
                self.display_text.setPlainText(text)
        except Exception:
            pass

    def clear_display(self):
        """action when the reset button is pressed"""
        self.path_input.clear()
        self.display_text.clear()
        self.privilege_check.setChecked(False)
        self.silent_check.setChecked(False)
        self.backup_check.setChecked(False)
        self.add_check.setChecked(False)
        self.loading_bar.hide()
        self.loading_label.hide()
        self.login_container.hide()
        self.login_secret.hide()

    def backupPath_show(self):
        """action when backup checkbox is toggled"""
        if self.backup_check.isChecked():
            self.backup_path_container.show()
        else:
            self.backup_path_container.hide()
            self.backup_path_input.setText("backups")

    def change_backup_path(self):
        """action when change backup path button is pressed"""
        path = QtWidgets.QFileDialog.getExistingDirectory(self, QtCore.QCoreApplication.translate(
            "script_dialog", "Choose the backup directory "))
        self.backup_path_input.setText(path)

    def apply_script(self):
        """action when the apply button is pressed"""
        self.display_text.clear()
        self.loading_label.show()
        self.commands = self.display_text.toPlainText().split('\n')
        self.loading_bar.setValue(0)
        self.toolbox.setEnabled(False)
        self.container.setEnabled(False)
        self.display_text.setReadOnly(True)
        self.loading_label.setText("Working on :" + self.ips[0])
        self.loading_container.show()
        self.loading_bar.show()
        if self.privilege_check.isChecked():
            self.login_secret.show()
        self._thread.start()
        self.request.emit([self.ips, self.commands, self.get_mode(), self.privilege_check.isChecked(), self.add_check.isChecked(
        ), self.silent_check.isChecked(), self.backup_check.isChecked, self.backup_path_input.text(), self.getInputs])

    def getInputs(self, data, mode="ask"):
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
            if self.privilege_check.isChecked():
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
                if self.privilege_check.isChecked() and self.device.myDb.all_info[index]["secret"] == '':
                    self.getInputs(data, mode='privilegeOnly')
                data = self.device.myDb.all_info[index].copy()
        self.reset_view()
        return data

    def toogle(self):
        """when confirm button is pressed"""
        self.loop = False

    def get_mode(self):
        """gets the input mode"""
        temp = self.select_mode.currentText()
        if temp == "Check login from the db":
            return "check"
        elif temp == "One login for all":
            return "one"
        else:
            return "ask"

    def reset_view(self):
        """when the inputs are done"""
        self.login_username.clear()
        self.login_username.show()
        self.login_password.clear()
        self.login_password.show()
        self.login_container.hide()
        self.login_secret.clear()
        self.login_secret.hide()

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
        self.container.setEnabled(True)
        self.loading_bar.setValue(0)
        self.loading_bar.hide()
        self.retry_btn.hide()
        self.loading_container.hide()
        self.clear_display()

    @QtCore.pyqtSlot()
    def after_work(self):
        self.display_text.setReadOnly(False)
        self.retry_btn.show()
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
        """         self.ips, self.commands, self.get_mode(), self.privilege_check.isChecked(), self.add_check.isChecked(), self.silent_check.isChecked(
                ), self.backup_check.isChecked, self.backup_path_input.text(), [self.loading_bar, self.loading_label, self.display_text], funct = self.getInputs """
        increment = [self.bar_signal, self.label_signal,
                     self.text_signal, self.done_signal]
        self.device.automate(args[0], args[1], args[2], args[3],
                             args[4], args[5], args[6], args[7], args[8], increment)

    @QtCore.pyqtSlot()
    def exit_process(self):
        print("Thread stopped")
        self.device.exit_process()
