from PyQt5 import QtCore, QtGui, QtWidgets
from backend.telnet import TelnetDevice


class Vlans_dialog(QtWidgets.QWidget):
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

    def setupUi(self, vlans_dialog):
            """the script dialog setup  """
        #main window
            vlans_dialog.setObjectName("vlans_dialog")
            vlans_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
            vlans_dialog.resize(543, 466)
        #main window vertical layout
            self.verticalLayout = QtWidgets.QVBoxLayout(vlans_dialog)
            self.verticalLayout.setObjectName("verticalLayout")
        #toolbox container
            self.toolbox = QtWidgets.QWidget(vlans_dialog)
            self.toolbox.setObjectName("toolbox")
        #toolbox horizontal layout
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.toolbox)
            self.horizontalLayout.setObjectName("horizontalLayout")
        #toolbox start input
            self.starting_label = QtWidgets.QLabel(self.toolbox)
            self.starting_label.setObjectName("starting_label")
            self.starting_label.setText("Starting vlan number")
            self.horizontalLayout.addWidget(self.starting_label)
            self.spinBox = QtWidgets.QSpinBox(self.toolbox)
            self.spinBox.setButtonSymbols(
                QtWidgets.QAbstractSpinBox.UpDownArrows)
            self.spinBox.setSpecialValueText("")
            self.spinBox.setAccelerated(False)
            self.spinBox.setSuffix("")
            self.spinBox.setMinimum(2)
            self.spinBox.setObjectName("spinBox")
            self.horizontalLayout.addWidget(self.spinBox)
         #toolbox number of vlans  input 
            self.increment_label = QtWidgets.QLabel(self.toolbox)
            self.increment_label.setObjectName("increment_label")
            self.increment_label.setText("Number of Vlans")
            self.horizontalLayout.addWidget(self.increment_label)
            self.spinBox1 = QtWidgets.QSpinBox(self.toolbox)
            self.spinBox1.setButtonSymbols(
                QtWidgets.QAbstractSpinBox.UpDownArrows)
            self.spinBox1.setSpecialValueText("")
            self.spinBox1.setAccelerated(False)
            self.spinBox1.setSuffix("")
            self.spinBox1.setMinimum(1)
            self.spinBox1.setObjectName("spinBox1")
            self.horizontalLayout.addWidget(self.spinBox1)
        #toolbox create vlans button
            self.createVlans_btn = QtWidgets.QPushButton(self.toolbox)
            self.createVlans_btn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.createVlans_btn.setObjectName("createVlans_btn")
            self.horizontalLayout.addWidget(self.createVlans_btn)
            self.createVlans_btn.clicked.connect(self.createVlans_script)
            self.verticalLayout.addWidget(self.toolbox)
        #loading label
            self.loading_label = QtWidgets.QLabel(vlans_dialog)
            self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
            self.loading_label.setObjectName("loading_label")
            self.loading_label.hide()
            self.verticalLayout.addWidget(self.loading_label)
        #loading container
            self.loading_container = QtWidgets.QWidget(vlans_dialog)
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
            self.login_container = QtWidgets.QWidget(vlans_dialog)
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
            self.display_text = QtWidgets.QTextEdit(vlans_dialog)
            self.display_text.setObjectName("display_text")
            self.display_text.setReadOnly(False)
            self.display_text.setPlaceholderText(
                "Input the name for each vlan here :")
            self.verticalLayout.addWidget(self.display_text)

            self.retranslateUi(vlans_dialog)
            QtCore.QMetaObject.connectSlotsByName(vlans_dialog)

    def retranslateUi(self, vlans_dialog):
        _translate = QtCore.QCoreApplication.translate
        vlans_dialog.setWindowTitle(_translate(
            "vlans_dialog", "Create Vlans "))
        self.createVlans_btn.setText(_translate("vlans_dialog", "Create"))
        self.loading_label.setText(_translate(
            "vlans_dialog", "Executing the script"))

    def createVlans_script(self):
        """action when the apply button is pressed"""
        self.name_list = self.display_text.toPlainText().split('\n')
        self.number = self.spinBox1.value()
        self.start = self.spinBox.value()
        if len(self.name_list) == self.number:
            self.display_text.clear()
            self.loading_label.show()
            self.loading_bar.setValue(0)
            self.toolbox.setEnabled(False)
            self.display_text.setReadOnly(True)
            self.loading_label.setText("Working on :" + self.ips[0])
            self.loading_container.show()
            self.loading_bar.show()
            self._thread.start()
            self.request.emit([self.ips, self.start, self.number, self.name_list, self.getInputs])
        else:
            self.loading_label.setText("The size of the inputs did not match the number of vlans")
            self.loading_label.show()

    def getInputs(self, data, mode="check"):
        """input the login info"""
        self.loop = True
        if mode == "ask":
            self.login_container.show()
            self.login_secret.show()
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
        self.spinBox.setValue(2)
        self.spinBox1.setValue(1)
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
        self.device.vlans(args[0], args[1], args[2], args[3],args[4], increment)

    @QtCore.pyqtSlot()
    def exit_process(self):
        print("Thread stopped")
        
