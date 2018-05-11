from PyQt5 import QtCore, QtGui, QtWidgets
import regex
from network_db.net_database import Net_db
import subprocess
import ipaddress
import functools



class Ui_Automate(QtWidgets.QWidget):
    """this is the automate widget """

    def __init__(self):
        """create the login page object"""
        QtWidgets.QWidget.__init__(
            self, None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        cur = Net_db()
        self.data = cur.getAll()
        self.ready = False
        self.select = False
        self.elements = []
        self.selected = []
        self.ip_from_db = cur.ips
        cur.closeDb()
        self.setupUi(self)

    def setupUi(self, Automate):
            """setup the interface of the automate window """
        #main widget
            Automate.setObjectName("Automate")
            Automate.resize(589, 465)
            Automate.setStyleSheet("background-color: rgb(30, 30, 30)")
        #main vertical layout
            self.verticalLayout = QtWidgets.QVBoxLayout(Automate)
            self.verticalLayout.setObjectName("verticalLayout")
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        #main toolbox
            self.toolbox = QtWidgets.QWidget(Automate)
            self.toolbox.setMinimumSize(QtCore.QSize(50, 50))
            """ #self.toolbox.setStyleSheet(
                "QPushButton{ color: rgb(25, 151, 198);border: none; padding:5px 0; font-size:16px;border-radius: 10px;}QPushButton:hover{background-color:rgb(50, 50, 50)}QPushButton:Pressed{border: 2px solid rgb(60, 60, 60)}") """
            self.toolbox.setObjectName("toolbox")
        #toolbox horizontal layout
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.toolbox)
            self.horizontalLayout.setObjectName("horizontalLayout")
        #toolbox select button
            self.select_btn = QtWidgets.QPushButton(self.toolbox)
            self.select_btn.setMinimumSize(QtCore.QSize(50, 50))
            self.select_btn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.select_btn.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("gui/img/cursor.png"),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.select_btn.setIcon(icon)
            self.select_btn.setIconSize(QtCore.QSize(30, 30))
            self.select_btn.setObjectName("select_btn")
            self.select_btn.setCheckable(True)
            self.select_btn.clicked.connect(self.select_btn_action)
            self.horizontalLayout.addWidget(self.select_btn)
        #toolbox from script button as script_btn
            self.script_btn = QtWidgets.QPushButton(self.toolbox)
            self.script_btn.setMinimumSize(QtCore.QSize(50, 50))
            self.script_btn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.script_btn.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("gui/img/script.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.script_btn.setIcon(icon1)
            self.script_btn.setIconSize(QtCore.QSize(30, 40))
            self.script_btn.setObjectName("script_btn")
            self.horizontalLayout.addWidget(self.script_btn)
        #toolbox invoque shell as invoqueShell_btn
            self.invoqueShell_btn = QtWidgets.QPushButton(self.toolbox)
            self.invoqueShell_btn.setMinimumSize(QtCore.QSize(50, 50))
            self.invoqueShell_btn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.invoqueShell_btn.setText("")
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("gui/img/terminal.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.invoqueShell_btn.setIcon(icon2)
            self.invoqueShell_btn.setIconSize(QtCore.QSize(40, 35))
            self.invoqueShell_btn.setObjectName("invoqueShell_btn")
            self.horizontalLayout.addWidget(self.invoqueShell_btn)
        #toolbox backup button as backup_btn
            self.backup_btn = QtWidgets.QPushButton(self.toolbox)
            self.backup_btn.setMinimumSize(QtCore.QSize(50, 50))
            self.backup_btn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.backup_btn.setText("")
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("gui/img/save.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.backup_btn.setIcon(icon3)
            self.backup_btn.setIconSize(QtCore.QSize(30, 30))
            self.backup_btn.setObjectName("backup_btn")
            self.horizontalLayout.addWidget(self.backup_btn)
        #toolbox restore button as restore_btn
            self.restore_btn = QtWidgets.QPushButton(self.toolbox)
            self.restore_btn.setMinimumSize(QtCore.QSize(50, 50))
            self.restore_btn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.restore_btn.setText("")
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap("gui/img/undo.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.restore_btn.setIcon(icon4)
            self.restore_btn.setIconSize(QtCore.QSize(30, 30))
            self.restore_btn.setObjectName("restore_btn")
            self.horizontalLayout.addWidget(self.restore_btn)
        #toolbox browse functions button as functions_btn
            self.functions_btn = QtWidgets.QPushButton(self.toolbox)
            self.functions_btn.setMinimumSize(QtCore.QSize(50, 50))
            self.functions_btn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.functions_btn.setText("")
            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap("gui/img/browser.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.functions_btn.setIcon(icon5)
            self.functions_btn.setIconSize(QtCore.QSize(30, 30))
            self.functions_btn.setObjectName("functions_btn")
            self.horizontalLayout.addWidget(self.functions_btn)
        #toolbox other options button as otherFn_btn
            self.otherFn_btn = QtWidgets.QPushButton(self.toolbox)
            self.otherFn_btn.setMinimumSize(QtCore.QSize(50, 50))
            self.otherFn_btn.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.otherFn_btn.setText("")
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("gui/img/menu(1).png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.otherFn_btn.setIcon(icon6)
            self.otherFn_btn.setIconSize(QtCore.QSize(30, 30))
            self.otherFn_btn.setObjectName("otherFn_btn")
            self.horizontalLayout.addWidget(self.otherFn_btn)
        #toolbox telnet radio button as telnet
            self.telnet = QtWidgets.QRadioButton(self.toolbox)
            self.telnet.setMinimumSize(QtCore.QSize(50, 50))
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setPointSize(12)
            self.telnet.setFont(font)
            self.telnet.setStyleSheet(
                "QRadioButton{background-color:rgb(30, 30, 30);color:rgb(255, 255, 255);}QRadioButton:indicator {width:10px;height:10px;border-radius:5px;}QRadioButton:indicator:checked {background-color:rgb(227, 0, 80);border:2px solid white;}QRadioButton:indicator:unchecked {background-color:rgb(255, 255, 255); border:2px solid white;}")
            self.telnet.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.telnet.setChecked(True)
            self.telnet.setObjectName("telnet")
            self.horizontalLayout.addWidget(self.telnet)
        #toolbox ssh radio button as ssh
            self.ssh = QtWidgets.QRadioButton(self.toolbox)
            self.ssh.setMinimumSize(QtCore.QSize(50, 50))
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setPointSize(12)
            self.ssh.setFont(font)
            self.ssh.setStyleSheet("QRadioButton{background-color:rgb(30, 30, 30);color:rgb(255, 255, 255);}QRadioButton:indicator {width:10px;height:10px;border-radius:5px;}QRadioButton:indicator:checked {background-color:rgb(227, 0, 80);border:2px solid white;}QRadioButton:indicator:unchecked {background-color:rgb(255, 255, 255); border:2px solid white;}")
            self.ssh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.ssh.setObjectName("ssh")
            self.horizontalLayout.addWidget(self.ssh)
            self.verticalLayout.addWidget(self.toolbox)
        #main automate tab as automate_tab
            self.automate_tab = QtWidgets.QTabWidget(Automate)
            self.automate_tab.setTabPosition(QtWidgets.QTabWidget.North)
            self.automate_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
            self.automate_tab.setIconSize(QtCore.QSize(10, 10))
            self.automate_tab.setElideMode(QtCore.Qt.ElideNone)
            self.automate_tab.setUsesScrollButtons(True)
            self.automate_tab.setDocumentMode(False)
            self.automate_tab.setTabsClosable(False)
            self.automate_tab.setMovable(False)
            self.automate_tab.setTabBarAutoHide(False)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setPointSize(11)
            self.automate_tab.setFont(font)
            self.automate_tab.setStyleSheet(
                "QTabWidget:pane{border-top:5px solid #2e2e2e}QWidget{background-color:rgb(46, 46, 46);color:white;}QTabBar:tab{background-color:rgb(60, 60, 60);color: white;padding: 10px ;qproperty-drawBase:0;}QTabBar:tab:selected{background-color:rgb(46, 46, 46)}")
            self.automate_tab.setObjectName("automate_tab")
        #from database widget as from_db
            self.from_db = QtWidgets.QWidget()
            self.from_db.setObjectName("from_db")
            self.from_db.setStyleSheet("QWidget{border-top:none}")
        #from database vertical layout
            self.from_db_layout = QtWidgets.QVBoxLayout(self.from_db)
            self.from_db_layout.setObjectName("from_db_layout")
        #from database check all checkbox as fromdb_checkall
            self.fromdb_checkall = QtWidgets.QCheckBox(self.from_db)
            self.fromdb_checkall.setTristate(False)
            self.fromdb_checkall.setChecked(False)
            self.fromdb_checkall.setStyleSheet(
                'margin-left: 5px; font: bold')
            self.fromdb_checkall.setText("Check All")
            self.fromdb_checkall.hide()
            self.fromdb_checkall.pressed.connect(self.checkall_db_action)
            self.from_db_layout.addWidget(self.fromdb_checkall)
        #from database scroll area
            self.scrollArea = QtWidgets.QScrollArea(self.from_db)
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setObjectName("scrollArea")
        #from database scroll area widget
            self.scrollAreaWidgetContents = QtWidgets.QWidget()
            self.scrollAreaWidgetContents.setGeometry(
                QtCore.QRect(0, 0, 545, 327))
            self.scrollAreaWidgetContents.setObjectName(
                "scrollAreaWidgetContents")
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.from_db_layout.addWidget(self.scrollArea)
            self.automate_tab.addTab(self.from_db, "")
        #from database grid layout AS gridLayout
            self.gridLayout = QtWidgets.QGridLayout(
                self.scrollAreaWidgetContents)
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setSpacing(0)
            self.gridLayout.setAlignment(QtCore.Qt.AlignTop)
            self.gridLayout.setObjectName("gridLayout")
        #from database devices
            self.putIngrid(self.gridLayout)
        #from file widget
            self.from_file = QtWidgets.QWidget()
            self.from_file.setObjectName("from_file")
            self.from_file.setStyleSheet("QWidget{border-top:none}")
        #from file horizontal layout
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.from_file)
            self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_2.setSpacing(0)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #from file widget container
            self.fromfile_container = QtWidgets.QWidget(self.from_file)
            self.fromfile_container.setObjectName("fromfile_container")
        #from file wigdet container vertical layout
            self.verticalLayout_2 = QtWidgets.QVBoxLayout(
                self.fromfile_container)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        #from file widget container toolbar
            self.fromfile_toolbar = QtWidgets.QWidget(self.fromfile_container)
            self.fromfile_toolbar.setObjectName("fromfile_toolbar")
        #from file toolbar horizontal layout
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(
                self.fromfile_toolbar)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        #from file toolbar path input as path_input
            self.path_input = QtWidgets.QLineEdit(self.fromfile_toolbar)
            self.path_input.setReadOnly(True)
            self.path_input.setMinimumSize(QtCore.QSize(300, 2))
            self.path_input.setText("")
            self.path_input.setObjectName("path_input")
            self.path_input.setStyleSheet(
                "QLineEdit{ margin:5px; color: white;border: 2px solid rgb(227, 0, 80); padding:5px; font-size:12px;border-radius: 10px;}QLineEdit:hover{background-color: rgb(30, 30, 30)}QLineEdit:Pressed{background-color: rgb(227, 0, 80)}")

            self.horizontalLayout_3.addWidget(self.path_input)
        #from file toolbar open button as file_open_btn
            self.file_open_btn = QtWidgets.QPushButton(self.fromfile_toolbar)
            self.file_open_btn.setObjectName("file_open_btn")
            self.file_open_btn.setMinimumWidth(100)
            self.file_open_btn.setStyleSheet(
                "QPushButton{ margin:5px; color: white;border: 2px solid rgb(227, 0, 80); padding:5px; font-size:12px;border-radius: 10px;}QPushButton:hover{background-color: rgb(30, 30, 30)}QPushButton:Pressed{background-color: rgb(227, 0, 80)}")
            self.horizontalLayout_3.addWidget(self.file_open_btn)
        #from file toolbar edit button as file_edit_btn
            self.file_edit_btn = QtWidgets.QPushButton(self.fromfile_toolbar)
            self.file_edit_btn.setObjectName("file_edit_btn")
            self.file_edit_btn.setMinimumWidth(100)
            self.horizontalLayout_3.addWidget(self.file_edit_btn)
            self.file_edit_btn.setStyleSheet(
                "QPushButton{ margin:5px;color: white;border: 2px solid rgb(227, 0, 80); padding:5px; font-size:12px;border-radius: 10px;}QPushButton:hover{background-color: rgb(30, 30, 30)}QPushButton:Pressed{background-color: rgb(227, 0, 80)}")
        #from file toolbar reset button as file_reset_btn
            self.file_reset_btn = QtWidgets.QPushButton(self.fromfile_toolbar)
            self.file_reset_btn.setObjectName("file_reset_btn")
            self.file_reset_btn.setMinimumWidth(100)
            self.horizontalLayout_3.addWidget(self.file_reset_btn)
            self.file_reset_btn.setStyleSheet(
                "QPushButton{ margin: 5px;color: white;border: 2px solid rgb(227, 0, 80); padding:5px; font-size:12px;border-radius: 10px;}QPushButton:hover{background-color: rgb(30, 30, 30)}QPushButton:Pressed{background-color: rgb(227, 0, 80)}")
        #from file toolbar apply button as file_apply_btn
            self.file_apply_btn = QtWidgets.QPushButton(self.fromfile_toolbar)
            self.file_apply_btn.setObjectName("file_apply_btn")
            self.file_apply_btn.setMinimumWidth(100)
            self.horizontalLayout_3.addWidget(self.file_apply_btn)
            self.file_apply_btn.setStyleSheet(
                "QPushButton{ margin: 5px;color: white;border: 2px solid rgb(227, 0, 80); padding:5px; font-size:12px;border-radius: 10px;}QPushButton:hover{background-color: rgb(30, 30, 30)}QPushButton:Pressed{background-color: rgb(227, 0, 80)}")
        #from file toolbar spacer item
            spacerItem = QtWidgets.QSpacerItem(
                40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_3.addItem(spacerItem)
            self.verticalLayout_2.addWidget(self.fromfile_toolbar)
        #from file check all checkbox button as file_checkall_btn
            self.file_checkall_btn = QtWidgets.QCheckBox(
                'Check All', self.fromfile_container)
            self.file_checkall_btn.setTristate(False)
            self.file_checkall_btn.setChecked(True)
            self.file_checkall_btn.setStyleSheet(
                'margin-left: 5px; font: bold')
            self.file_checkall_btn.hide()
            self.verticalLayout_2.addWidget(self.file_checkall_btn)
        #from file toolbar events handler
            self.file_open_btn.setDefault(True)
            self.file_open_btn.clicked.connect(self.choose_file_action)
            self.file_edit_btn.clicked.connect(self.edit_file_action)
            self.file_reset_btn.clicked.connect(self.reset_file_action)
            self.file_apply_btn.clicked.connect(self.apply_file_action)
            self.file_checkall_btn.clicked.connect(
                self.selectAllCheckChanged_action)
        #from file text view as fromfile_view
            self.fromfile_view = QtWidgets.QTextEdit(self.fromfile_container)
            self.fromfile_view.setReadOnly(True)
            self.fromfile_view.setObjectName("fromfile_view")
            self.verticalLayout_2.addWidget(self.fromfile_view)
            self.horizontalLayout_2.addWidget(self.fromfile_container)
        #from file list ip table widget as self.fromfile_ips
            self.fromfile_ips = QtWidgets.QTableWidget(self.fromfile_container)
            self.fromfile_ips.setColumnCount(3)
            self.fromfile_ips.verticalHeader().hide()
            self.fromfile_ips.setHorizontalHeaderLabels(
                ['ip address', 'Is in the DB?', 'Is Connected?'])
            fromfile_header = self.fromfile_ips.horizontalHeader()
            fromfile_header.setSectionResizeMode(
                0, QtWidgets.QHeaderView.Stretch)
            fromfile_header.setSectionResizeMode(
                1, QtWidgets.QHeaderView.ResizeToContents)
            fromfile_header.setSectionResizeMode(
                2, QtWidgets.QHeaderView.ResizeToContents)
            self.fromfile_ips.setObjectName("fromfile_ips")
            self.fromfile_ips.clicked.connect(self.checkall_file_action)
            self.fromfile_ips.hide()
            self.verticalLayout_2.addWidget(self.fromfile_ips)
        #from range widget
            self.automate_tab.addTab(self.from_file, "")
            self.from_range = QtWidgets.QWidget()
            self.from_range.setObjectName("from_range")
            self.from_range.setStyleSheet("QWidget{border-top:none}")
            self.from_range.setStyleSheet(
                "QPushButton{ margin:3px; color: white;border: 2px solid rgb(227, 0, 80); padding:5px; font-size:12px;border-radius: 10px;}QPushButton:hover{background-color: rgb(30, 30, 30)}QPushButton:Pressed{background-color: rgb(227, 0, 80)}")
        #from range horizontal layout
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.from_range)
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        #from range container as fromrange_container
            self.fromrange_container = QtWidgets.QWidget(self.from_range)
            self.fromrange_container.setObjectName("fromrange_container")
            self.fromrange_container.setContentsMargins(0, 0, 0, 0)
            self.fromrange_container.setStyleSheet("QWidget{border:none}")
        #from range container vertical layout
            self.verticalLayout_5 = QtWidgets.QVBoxLayout(
                self.fromrange_container)
            self.verticalLayout_5.setObjectName("verticalLayout_5")
            self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        #from range toolbar
            self.fromrange_toolbar = QtWidgets.QWidget(
                self.fromrange_container)
            self.fromrange_toolbar.setObjectName("fromrange_toolbar")
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setPointSize(14)
            self.fromrange_toolbar.setFont(font)
            self.fromrange_toolbar.setStyleSheet(
                "QPushButton{ margin:3px; color: white;border: 2px solid rgb(227, 0, 80); padding:5px; font-size:12px;border-radius: 10px;}QPushButton:hover{background-color: rgb(30, 30, 30)}QPushButton:Pressed{background-color: rgb(227, 0, 80)}")
        #from range toolbar horizontal layout
            self.horizontalLayout_5 = QtWidgets.QHBoxLayout(
                self.fromrange_toolbar)
            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        #from range toolbar range label as range_label
            self.range_label = QtWidgets.QLabel(self.fromrange_toolbar)
            self.range_label.setObjectName("range_label")
            self.horizontalLayout_5.addWidget(self.range_label)
        #from range toolbar starting address input as start_address_input
            self.start_address_input = QtWidgets.QLineEdit(
                self.fromrange_toolbar)
            self.start_address_input.setObjectName("start_address_input")
            self.horizontalLayout_5.addWidget(self.start_address_input)
            self.start_address_input.setStyleSheet(
                "QLineEdit{ margin:5px; color: white;border: 2px solid rgb(227, 0, 80); padding:5px; font-size:12px;border-radius: 10px;}QLineEdit:hover{background-color: rgb(30, 30, 30)}QLineEdit:Pressed{background-color: rgb(227, 0, 80)}")
        #from range toolbar ending address input as end_address_input
            self.end_address_input = QtWidgets.QLineEdit(
                self.fromrange_toolbar)
            self.end_address_input.setObjectName("end_address_input")
            self.horizontalLayout_5.addWidget(self.end_address_input)
            self.end_address_input.setStyleSheet(
                "QLineEdit{ margin:5px; color: white;border: 2px solid rgb(227, 0, 80); padding:5px; font-size:12px;border-radius: 10px;}QLineEdit:hover{background-color: rgb(30, 30, 30)}QLineEdit:Pressed{background-color: rgb(227, 0, 80)}")
        #from range toolbar increment label as increment_label
            self.increment_label = QtWidgets.QLabel(self.fromrange_toolbar)
            self.increment_label.setObjectName("increment_label")
            self.horizontalLayout_5.addWidget(self.increment_label)
            self.spinBox_3 = QtWidgets.QSpinBox(self.fromrange_toolbar)
            self.spinBox_3.setButtonSymbols(
                QtWidgets.QAbstractSpinBox.UpDownArrows)
            self.spinBox_3.setSpecialValueText("")
            self.spinBox_3.setAccelerated(False)
            self.spinBox_3.setSuffix("")
            self.spinBox_3.setMinimum(1)
            self.spinBox_3.setObjectName("spinBox_3")
            self.horizontalLayout_5.addWidget(self.spinBox_3)
            self.spinBox_3.setStyleSheet(
                "QSpinBox{ background-color:rgb(60, 60, 60);margin:5px; color: white;border: none; padding:2px; font-size:12px;border-radius: 20px;}QSpinBox:hover{background-color: rgb(30, 30, 30)}")
        #from range toolbar reset buttons as range_reset_btn
            self.range_reset_btn = QtWidgets.QPushButton(self.fromfile_toolbar)
            self.range_reset_btn.setObjectName("range_reset_btn")
            self.horizontalLayout_5.addWidget(self.range_reset_btn)
            self.range_reset_btn.setMinimumWidth(60)
            self.verticalLayout_5.addWidget(self.fromrange_toolbar)
        #from range toolbar apply buttons as range_apply_btn
            self.range_apply_btn = QtWidgets.QPushButton(self.fromfile_toolbar)
            self.range_apply_btn.setObjectName("range_apply_btn")
            self.range_apply_btn.setMinimumWidth(60)
            self.horizontalLayout_5.addWidget(self.range_apply_btn)
        #from file check all checkbox button as range_checkall_btn
            self.range_checkall_btn = QtWidgets.QCheckBox(
                'Check All', self.fromrange_container)
            self.range_checkall_btn.setTristate(False)
            self.range_checkall_btn.setChecked(True)
            self.range_checkall_btn.setStyleSheet(
                'margin-left: 5px; font: bold')
            self.range_checkall_btn.hide()
            self.verticalLayout_5.addWidget(self.range_checkall_btn)
        #from range list view as fromrange_view
            self.fromrange_view = QtWidgets.QListView(self.fromrange_container)
            self.fromrange_view.setObjectName("fromrange_view")
            self.verticalLayout_5.addWidget(self.fromrange_view)
            self.horizontalLayout_4.addWidget(self.fromrange_container)
            self.automate_tab.addTab(self.from_range, "")
            self.verticalLayout.addWidget(self.automate_tab)
        #from range list ip table widget as self.fromrange_ips
            self.fromrange_ips = QtWidgets.QTableWidget(
                self.fromrange_container)
            self.fromrange_ips.setColumnCount(3)
            self.fromrange_ips.verticalHeader().hide()
            self.fromrange_ips.setHorizontalHeaderLabels(
                ['Ip address', 'Is in the DB?', 'Is Connected?'])
            fromrange_header = self.fromrange_ips.horizontalHeader()
            fromrange_header.setSectionResizeMode(
                0, QtWidgets.QHeaderView.Stretch)
            fromrange_header.setSectionResizeMode(
                1, QtWidgets.QHeaderView.ResizeToContents)
            fromrange_header.setSectionResizeMode(
                2, QtWidgets.QHeaderView.ResizeToContents)
            self.fromrange_ips.setObjectName("fromrange_ips")
            self.fromrange_ips.hide()
            self.verticalLayout_5.addWidget(self.fromrange_ips)
        #from range toolbar connect functions
            self.range_apply_btn.setDefault(True)
            self.range_apply_btn.clicked.connect(self.apply_range_action)
            self.range_reset_btn.clicked.connect(self.reset_range_action)
            self.range_checkall_btn.clicked.connect(self.checkall_range_action)
            self.fromrange_ips.clicked.connect(self.unchecked_range_action)
        #other options
            self.retranslateUi(Automate)
            self.automate_tab.setCurrentIndex(0)
            QtCore.QMetaObject.connectSlotsByName(Automate)
            Automate.setTabOrder(self.start_address_input,
                                 self.end_address_input)
            Automate.setTabOrder(self.end_address_input, self.spinBox_3)
            Automate.setTabOrder(self.spinBox_3, self.fromrange_view)
            Automate.setTabOrder(self.fromrange_view, self.select_btn)
            Automate.setTabOrder(self.select_btn, self.script_btn)
            Automate.setTabOrder(self.script_btn, self.invoqueShell_btn)
            Automate.setTabOrder(self.invoqueShell_btn, self.backup_btn)
            Automate.setTabOrder(self.backup_btn, self.restore_btn)
            Automate.setTabOrder(self.restore_btn, self.functions_btn)
            Automate.setTabOrder(self.functions_btn, self.otherFn_btn)
            Automate.setTabOrder(self.otherFn_btn, self.telnet)
            Automate.setTabOrder(self.telnet, self.ssh)
            Automate.setTabOrder(self.ssh, self.automate_tab)
            Automate.setTabOrder(self.automate_tab, self.fromfile_view)
            Automate.setTabOrder(self.fromfile_view, self.scrollArea)
            Automate.setTabOrder(self.scrollArea, self.path_input)

    def retranslateUi(self, Automate):
        """setting the labels and titles """
        _translate = QtCore.QCoreApplication.translate
        Automate.setWindowTitle(_translate("Automate", "Automate"))
        self.select_btn.setToolTip(_translate(
            "Automate", "<html><head/><body><p>Select devices</p></body></html>"))
        self.script_btn.setToolTip(_translate(
            "Automate", "<html><head/><body><p><span style=\" font-size:10pt;\">apply commands from script</span></p></body></html>"))
        self.invoqueShell_btn.setToolTip(_translate(
            "Automate", "<html><head/><body><p>Invoque shell</p></body></html>"))
        self.backup_btn.setToolTip(_translate(
            "Automate", "<html><head/><body><p>Backup configuration</p></body></html>"))
        self.restore_btn.setToolTip(_translate(
            "Automate", "<html><head/><body><p>Restore configuration</p></body></html>"))
        self.functions_btn.setToolTip(_translate(
            "Automate", "<html><head/><body><p>Browse commun tasks</p></body></html>"))
        self.otherFn_btn.setToolTip(_translate(
            "Automate", "<html><head/><body><p>Other options</p></body></html>"))
        self.telnet.setToolTip(_translate(
            "Automate", "<html><head/><body><p>select telnet connection</p></body></html>"))
        self.telnet.setText(_translate("Automate", "Telnet"))
        self.ssh.setToolTip(_translate(
            "Automate", "<html><head/><body><p>Select ssh connection</p></body></html>"))
        self.ssh.setText(_translate("Automate", "SSH"))
        self.automate_tab.setTabText(self.automate_tab.indexOf(
            self.from_db), _translate("Automate", "IP from database"))
        self.path_input.setPlaceholderText(_translate(
            "Automate", "File path , Please press Open --->"))
        self.file_open_btn.setText(_translate("Automate", "Open"))
        self.file_apply_btn.setText(_translate("Automate", "Apply"))
        self.file_edit_btn.setText(_translate("Automate", "Edit"))
        self.file_reset_btn.setText(_translate("Automate", "Reset"))
        self.automate_tab.setTabText(self.automate_tab.indexOf(
            self.from_file), _translate("Automate", "IP from a file"))
        self.range_label.setText(_translate("Automate", "Range"))
        self.start_address_input.setPlaceholderText(
            _translate("Automate", "Starting ip address..."))
        self.end_address_input.setPlaceholderText(
            _translate("Automate", "Ending ip address..."))
        self.increment_label.setText(_translate("Automate", "Increment :"))
        self.range_reset_btn.setText(_translate("Automate", "Reset"))
        self.range_apply_btn.setText(_translate("Automate", "Apply"))
        self.automate_tab.setTabText(self.automate_tab.indexOf(
            self.from_range), _translate("Automate", "IP from a range"))

    #from db item container
    def putIngrid(self, grid):
        """puts all data in the grid layout"""
        max_column = 4
        j = 0
        i = 0
        for x, item in enumerate(self.data):
            if i == max_column:
                j += 1
                i = 0
            element = self.from_db_object(item)
            element.clicked.connect(functools.partial(
                self.fromdb_isChecked_action, x))
            grid.addWidget(element, j, i)
            self.elements.append(element)
            i += 1

    def checkall_db_action(self):
        """when check all from db is checked"""
        if not self.fromdb_checkall.isChecked():
            for element in self.elements:
                element.setChecked(True)
            self.selected = self.data.copy()
        else:
            for element in self.elements:
                element.setChecked(False)
            self.selected = []

    def fromdb_isChecked_action(self, x):
        """when the element is checked"""
        item = self.elements[x]
        if not item.isChecked():
            self.fromdb_checkall.setChecked(False)

    def from_db_object(self, data):
        """create an object view for from database tab"""
        #item container
        container = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        vertical = QtWidgets.QVBoxLayout(container)
        container.setCheckable(False)
        #image label
        img = QtWidgets.QLabel(container)
        if data["type"] == 'switch':
            img.setPixmap(QtGui.QPixmap("gui/img/switchIcon.png"))
        else:
            img.setPixmap(QtGui.QPixmap("gui/img/routerIcon.png"))
        img.setMaximumHeight(100)
        img.setScaledContents(True)
        #connect push button
        btn = QtWidgets.QPushButton(container)
        btn.setText("Connect")
        if self.ping(data["ip"]):
            btn.setStyleSheet("color: green;")
        else:
            btn.setStyleSheet("color: red;")
        #checkbox
        check = QtWidgets.QCheckBox(container)
        check.hide()
        #table widget
        table = QtWidgets.QTableWidget(container)
        table.setColumnCount(1)
        table.setRowCount(3)
        head = table.horizontalHeader()
        head.hide()
        head.setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        table.setVerticalHeaderLabels(
            ['IP address', 'Host', 'Description'])
        item_ip = QtWidgets.QTableWidgetItem(data["ip"])
        item_ip.setFlags(QtCore.Qt.ItemIsEnabled)
        item_host = QtWidgets.QTableWidgetItem(data["host"])
        item_host.setFlags(QtCore.Qt.ItemIsEnabled)
        item_description = QtWidgets.QTableWidgetItem(data["description"])
        item_description.setFlags(QtCore.Qt.ItemIsEnabled)
        table.setItem(0, 0, item_ip)
        table.setItem(0, 1, item_host)
        table.setItem(0, 2, item_description)
        #adding to layout
        vertical.addWidget(img)
        vertical.addWidget(check)
        vertical.addWidget(table)
        vertical.addWidget(btn)
        container.setMinimumSize(120, 260)
        return container

    #event functions
    #from file actions
    def choose_file_action(self):
        """action when from file open button is pressed"""
        self.switchview_file(self.fromfile_view,
                             self.fromfile_ips, self.file_checkall_btn, False)
        path = QtWidgets.QFileDialog.getOpenFileName(self, QtCore.QCoreApplication.translate(
            "Automate", "Choose the ip addresses file "), "backend/", QtCore.QCoreApplication.translate("Automate", "Text File(*.txt)"))[0]
        self.path_input.setText(path)
        try:
            with open(path, 'r') as f:
                text = ''.join(f.readlines())
                self.fromfile_view.setReadOnly(True)
                self.fromfile_view.setPlainText(text)
                ##changes!!! restorer le style de self.fromfile_view
        except Exception:
            pass

    def edit_file_action(self):
        """action when from file edit button is pressed"""
        self.switchview_file(self.fromfile_view,
                             self.fromfile_ips, self.file_checkall_btn, False)
        self.fromfile_view.setReadOnly(False)
        ##changes!!! changer la couleur de fond de self.fromfile_view

    def reset_file_action(self):
        """action when from file reset button is pressed"""
        self.switchview_file(self.fromfile_view,
                             self.fromfile_ips, self.file_checkall_btn, False)
        self.fromfile_view.clear()
        self.fromfile_view.setReadOnly(True)
        self.path_input.clear()

    def apply_file_action(self):
        """action when from file apply button is pressed"""
        #getting the ips from the widget
        ips = [item for item in (
            self.fromfile_view.toPlainText().split('\n')) if self.check_ip(item)]
        self.all_selections = ips.copy()
        self.selected = ips.copy()
        if ips:
            self.fillTablewithIps(self.fromfile_ips, ips)
            #display the table and hide the view
            self.switchview_file(
                self.fromfile_view, self.fromfile_ips, self.file_checkall_btn, True)
        else:
            self.errorMsg("No valid ip found in the section")

    def checkall_file_action(self):
        """when the row ip is clicked """
        model = self.fromfile_ips
        item = model.currentColumn()
        if item == -1:
            self.file_checkall_btn.setCheckState(QtCore.Qt.Unchecked)

    def selectAllCheckChanged_action(self):
        """from file when check all button is pressed"""
        model = self.fromfile_ips
        if self.file_checkall_btn.isChecked():
            state = QtCore.Qt.Checked
        else:
            state = QtCore.Qt.Unchecked
        for index in range(model.rowCount()):
            item = model.item(index, 0)
            item.setCheckState(state)

    #from range actions
    def apply_range_action(self):
        """action when from range apply button is pressed"""
        start = self.start_address_input.text()
        end = self.end_address_input.text()
        increment = int(self.spinBox_3.value())
        self.fromrange_ips.setRowCount(0)
        ips = self.generateRange(start, end, increment)
        if ips:
            self.fillTablewithIps(self.fromrange_ips, ips)
            self.switchview_file(
                self.fromrange_view, self.fromrange_ips, self.range_checkall_btn, True)
        else:
            self.errorMsg("No valid ip found in the section")

    def reset_range_action(self):
        """action when from range reset button is pressed"""
        self.start_address_input.setText('')
        self.end_address_input.setText('')
        self.spinBox_3.setValue(1)
        self.range_checkall_btn.hide()
        self.switchview_file(self.fromrange_view,
                             self.fromrange_ips, self.file_checkall_btn, False)

    def checkall_range_action(self):
        """action when the range check_all btn is pressed"""
        model = self.fromrange_ips
        if self.range_checkall_btn.isChecked():
            state = QtCore.Qt.Checked
        else:
            state = QtCore.Qt.Unchecked
        for index in range(model.rowCount()):
            item = model.item(index, 0)
            item.setCheckState(state)

    def unchecked_range_action(self):
        """when the row ip is clicked """
        model = self.fromrange_ips
        item = model.currentItemChanged
        if item == -1:
            self.range_checkall_btn.setCheckState(QtCore.Qt.Unchecked)

    #main toolbar actions
    def select_btn_action(self):
        """this is when the select button is pressed"""
        if self.select_btn.isChecked():
            self.show_checkable()
            self.select_btn.setChecked(True)     
        else:
            self.hide_checkable()
            self.select_btn.setChecked(False)

    #utiliy functions
    def fillTablewithIps(self, table, ips):
        """create cases of a table and fill it with ips, checkboxes, is in db and is connected"""
        #creating rows
        ip_size = len(ips)
        table.setRowCount(ip_size)
        for i, ip in enumerate(ips):
            #creating items
            item_ip = QtWidgets.QTableWidgetItem(ip)
            item_ip.setFlags(QtCore.Qt.ItemIsEnabled)
            inDb = QtWidgets.QTableWidgetItem(self.checkIpInDb(ip))
            inDb.setFlags(QtCore.Qt.ItemIsEnabled)
            if ip_size < 15:
                connected = QtWidgets.QTableWidgetItem(
                    self.checkIpConnected(ip))
            else:
                connected = QtWidgets.QTableWidgetItem("Timeout")
            connected.setFlags(QtCore.Qt.ItemIsEnabled)
            #adding the items to the table
            table.setItem(i, 0, item_ip)
            table.setItem(i, 1, inDb)
            table.setItem(i, 2, connected)

    def checkIpInDb(self, ip):
        """checks if the ip is in the db """
        if ip in self.ip_from_db:
            return "Yes"
        else:
            return "No"

    def ping(self, ip):
        """ping the device"""
        system = subprocess.sys.platform.lower()
        if system.startswith('win'):
            info = subprocess.STARTUPINFO()
            info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            info.wShowWindow = subprocess.SW_HIDE
            # run the ping command with subprocess.popen interface
            output = subprocess.Popen(['ping', '-n', '1', '-w', '500', ip],
                                    stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
            if "Destination host unreachable" in output.decode('utf-8'):
                return False
            elif "Request timed out" in output.decode('utf-8'):
                return False
            else:
                return True
        else:
            output = subprocess.Popen(['ping', '-w', '1', ip],
                                    stdout=subprocess.PIPE).communicate()[0]
            if "100% packet loss" in output.decode('utf-8').lower():
                return False
            else:
                return True
                
    def checkIpConnected(self, ip):
        """checks if the ip is connected"""
        result = self.ping(ip)
        if result:
            return "Yes"
        else:
            return "No"

    def switchview_file(self, listview, tableview, checkall_btn, goIp):
        """switch between list view and text edit"""
        self.select_btn.setChecked(False)
        if goIp:
            listview.hide()
            tableview.show()
        else:
            checkall_btn.hide()
            listview.show()
            tableview.hide()

    def check_ip(self, text):
        """check if the text is a valid ip address"""
        #         pattern = regex.compile(
        #           return regex.fullmatch(pattern, text)
        #          r"(^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$)")
        try:
            ipaddress.IPv4Address(text)
        except Exception:
            return False
        return True

    def errorMsg(self, msg):
        """display an error msg to the screen"""
        QtWidgets.QMessageBox.warning(
            self, "Login", msg, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def generateRange(self, start, end, increment):
        """return a list of ips from a given interval"""
        ips = []
        if self.check_ip(start) and self.check_ip(end):
            starting = ipaddress.ip_address(start)
            ending = ipaddress.ip_address(end)
            if (int(ending)-int(starting)) < 300:
                try:
                    while starting <= ending:
                        ip = starting.compressed
                        ips.append(ip)
                        starting += increment
                except Exception:
                    return None
        else:
            return None
        return ips

    def show_checkable(self):
        """shows the checkable items"""
        if self.automate_tab.currentIndex() == 0:
            self.fromdb_checkall.show()
            for i in range(self.gridLayout.count()):
                self.gridLayout.itemAt(i).widget().setCheckable(True)
        elif self.automate_tab.currentIndex() == 1:
            if self.fromfile_ips.isVisible():
                self.file_checkall_btn.show()
                for i in range(self.fromfile_ips.rowCount()):
                    self.fromfile_ips.item(i, 0).setFlags(
                        QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
                    self.fromfile_ips.item(
                        i, 0).setCheckState(QtCore.Qt.Checked)
        elif self.automate_tab.currentIndex() == 2:
            if self.fromrange_ips.isVisible():
                self.range_checkall_btn.show()
                for i in range(self.fromrange_ips.rowCount()):
                    self.fromrange_ips.item(i, 0).setFlags(
                        QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
                    self.fromrange_ips.item(
                        i, 0).setCheckState(QtCore.Qt.Checked)

    def hide_checkable(self):
        """hide the checkable items""" 
        self.select_btn.setChecked(False)
        if self.automate_tab.currentIndex() == 0:
            self.fromdb_checkall.hide()
            for i in range(self.gridLayout.count()):
                self.gridLayout.itemAt(i).widget().setCheckable(False)
        elif self.automate_tab.currentIndex() == 1:
            if self.fromfile_ips.isVisible():
                self.file_checkall_btn.hide()
                for i in range(self.fromfile_ips.rowCount()):
                    flags = self.fromfile_ips.item(i, 0).flags()
                    flags &= ~QtCore.Qt.ItemIsEnabled
                    flags &= ~QtCore.Qt.ItemIsUserCheckable
                    self.fromfile_ips.item(i, 0).setFlags(flags)
        elif self.automate_tab.currentIndex() == 2:
            if self.fromrange_ips.isVisible():
                self.range_checkall_btn.hide()
                for i in range(self.fromrange_ips.rowCount()):
                    flags = self.fromrange_ips.item(i, 0).flags()
                    flags &= ~QtCore.Qt.ItemIsEnabled
                    flags &= ~QtCore.Qt.ItemIsUserCheckable
                    self.fromrange_ips.item(i, 0).setFlags(flags)
                      
    def get_selected(self):
        """get the list of selected ips """
        self.selected = []
        if self.automate_tab.currentIndex() == 0:
            for i in range(self.gridLayout.count()):
                item = self.gridLayout.itemAt(i)
                if item.widget().isChecked():
                    self.selected.append(item.widget().children()[
                                         4].itemAt(0, 0).text())
        elif self.automate_tab.currentIndex() == 1:
            for i in range(self.fromfile_ips.rowCount()):
                if self.fromfile_ips.item(i, 0).checkState():
                    self.selected.append(self.fromfile_ips.item(i, 0).text())
        elif self.automate_tab.currentIndex() == 2:
            for i in range(self.fromrange_ips.rowCount()):
                if self.fromrange_ips.item(i, 0).checkState():
                    self.selected.append(self.fromrange_ips.item(i, 0).text())

    def checkin_selection(self):
        """checks if teh user is in selection mode"""
        pass
