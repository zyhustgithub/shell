# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'breack.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 338)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/backup/static/Mug-PNG.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-image : url(/static/loading.gif);\n"
"    background-attachment : fixed;\n"
"    background-position : 5% 80%; \n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_main = QtWidgets.QHBoxLayout()
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")
        self.formGroupBox_tab_l = QtWidgets.QGroupBox(self.centralwidget)
        self.formGroupBox_tab_l.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formGroupBox_tab_l.sizePolicy().hasHeightForWidth())
        self.formGroupBox_tab_l.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.formGroupBox_tab_l.setFont(font)
        self.formGroupBox_tab_l.setObjectName("formGroupBox_tab_l")
        self.horizontalLayout_left = QtWidgets.QHBoxLayout(self.formGroupBox_tab_l)
        self.horizontalLayout_left.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_left.setObjectName("horizontalLayout_left")
        self.tabWidget_left = QtWidgets.QTabWidget(self.formGroupBox_tab_l)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_left.setFont(font)
        self.tabWidget_left.setStyleSheet("QTabBar::tab {\n"
"    min-width:25px;\n"
"    background-color: white;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    padding-top: -10px;\n"
"    padding-bottom: 5px;\n"
"    border-right: 3px solid white;\n"
"}    \n"
"QTabBar::tab:!selected {\n"
"    margin-left: 0px;\n"
"} \n"
"QTabBar::tab:selected {\n"
"    background-color: white;\n"
"    border-right: 3px solid green;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    border-right: 3px solid orange;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;    \n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"     right: 0px; /* move to the right by 5px */\n"
" }\n"
" ")
        self.tabWidget_left.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_left.setIconSize(QtCore.QSize(80, 20))
        self.tabWidget_left.setTabsClosable(False)
        self.tabWidget_left.setTabBarAutoHide(False)
        self.tabWidget_left.setObjectName("tabWidget_left")
        self.tab_l1 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_l1.sizePolicy().hasHeightForWidth())
        self.tab_l1.setSizePolicy(sizePolicy)
        self.tab_l1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab_l1.setObjectName("tab_l1")
        self.horizontalLayout_tab_l1 = QtWidgets.QHBoxLayout(self.tab_l1)
        self.horizontalLayout_tab_l1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_tab_l1.setSpacing(4)
        self.horizontalLayout_tab_l1.setObjectName("horizontalLayout_tab_l1")
        self.frame = QtWidgets.QFrame(self.tab_l1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(-1, 6, 6, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_tab_l1.addWidget(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("static/recent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_left.addTab(self.tab_l1, icon1, "")
        self.tab_l2 = QtWidgets.QWidget()
        self.tab_l2.setObjectName("tab_l2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_l2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.tab_l2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2.addWidget(self.frame_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("static/Star.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_left.addTab(self.tab_l2, icon2, "")
        self.horizontalLayout_left.addWidget(self.tabWidget_left)
        self.horizontalLayout_main.addWidget(self.formGroupBox_tab_l)
        self.tabWidget_right = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_right.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_right.setFont(font)
        self.tabWidget_right.setStyleSheet("QTabBar::tab {\n"
"    min-height:20px;\n"
"    background-color: white;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    border-bottom: 3px solid white;\n"
"}    \n"
"QTabBar::tab:!selected {\n"
"    margin-top: 0px;\n"
"} \n"
"QTabBar::tab:!selected:hover {\n"
"    border-bottom: 3px solid orange;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background-color: white;\n"
"    border-bottom: 3px solid green;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
" QTabWidget::tab-bar {\n"
"     left: 0px; /* move to the right by 5px */\n"
" }\n"
"")
        self.tabWidget_right.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_right.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_right.setTabsClosable(True)
        self.tabWidget_right.setMovable(True)
        self.tabWidget_right.setObjectName("tabWidget_right")
        self.tab_r1 = QtWidgets.QWidget()
        self.tab_r1.setObjectName("tab_r1")
        self.gridLayout_tab_r1 = QtWidgets.QGridLayout(self.tab_r1)
        self.gridLayout_tab_r1.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_tab_r1.setHorizontalSpacing(0)
        self.gridLayout_tab_r1.setObjectName("gridLayout_tab_r1")
        self.formGroupBox_tab_r1_1 = QtWidgets.QGroupBox(self.tab_r1)
        self.formGroupBox_tab_r1_1.setObjectName("formGroupBox_tab_r1_1")
        self.horizontalLayout_middle = QtWidgets.QHBoxLayout(self.formGroupBox_tab_r1_1)
        self.horizontalLayout_middle.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_middle.setObjectName("horizontalLayout_middle")
        self.label = QtWidgets.QLabel(self.formGroupBox_tab_r1_1)
        self.label.setObjectName("label")
        self.horizontalLayout_middle.addWidget(self.label)
        self.dateEdit = QtWidgets.QDateEdit(self.formGroupBox_tab_r1_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_middle.addWidget(self.dateEdit)
        self.lineEdit = QtWidgets.QLineEdit(self.formGroupBox_tab_r1_1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_middle.addWidget(self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(self.formGroupBox_tab_r1_1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_middle.addWidget(self.pushButton_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_middle.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.formGroupBox_tab_r1_1)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_middle.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.formGroupBox_tab_r1_1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_middle.addWidget(self.pushButton_2)
        self.gridLayout_tab_r1.addWidget(self.formGroupBox_tab_r1_1, 1, 0, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_r1)
        self.tableWidget.setStyleSheet("selection-background-color: rgb(238, 233, 233);\n"
"selection-color: rgb(0, 0, 0);")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(11)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.PartiallyChecked)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.gridLayout_tab_r1.addWidget(self.tableWidget, 0, 1, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_r1)
        self.treeWidget.setStyleSheet("selection-background-color: rgb(238, 233, 233);\n"
"selection-color: rgb(0, 0, 0);")
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "选项")
        self.treeWidget.headerItem().setText(1, "名称")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Checked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Checked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Checked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Checked)
        self.gridLayout_tab_r1.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.tab_r1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar::chunk{background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 orange,stop:1 red);}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_tab_r1.addWidget(self.progressBar, 3, 0, 1, 2)
        self.formGroupBox_tab_r1_2 = QtWidgets.QGroupBox(self.tab_r1)
        self.formGroupBox_tab_r1_2.setMinimumSize(QtCore.QSize(0, 120))
        self.formGroupBox_tab_r1_2.setObjectName("formGroupBox_tab_r1_2")
        self.horizontalLayout_bottom = QtWidgets.QHBoxLayout(self.formGroupBox_tab_r1_2)
        self.horizontalLayout_bottom.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_bottom.setObjectName("horizontalLayout_bottom")
        self.textEdit = QtWidgets.QTextEdit(self.formGroupBox_tab_r1_2)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_bottom.addWidget(self.textEdit)
        self.gridLayout_tab_r1.addWidget(self.formGroupBox_tab_r1_2, 2, 0, 1, 2)
        self.gridLayout_tab_r1.setColumnStretch(0, 1)
        self.gridLayout_tab_r1.setColumnStretch(1, 4)
        self.gridLayout_tab_r1.setRowStretch(0, 4)
        self.gridLayout_tab_r1.setRowStretch(2, 1)
        self.tabWidget_right.addTab(self.tab_r1, "")
        self.tab_r2 = QtWidgets.QWidget()
        self.tab_r2.setObjectName("tab_r2")
        self.tabWidget_right.addTab(self.tab_r2, "")
        self.tab_r3 = QtWidgets.QWidget()
        self.tab_r3.setObjectName("tab_r3")
        self.tabWidget_right.addTab(self.tab_r3, "")
        self.horizontalLayout_main.addWidget(self.tabWidget_right)
        self.horizontalLayout_main.setStretch(0, 1)
        self.horizontalLayout_main.setStretch(1, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 18))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("QMenuBar{\n"
"    background-color: rgb(129, 198, 223);\n"
"}\n"
"QMenuBar:selected {\n"
"    selection-background-color: rgb(255, 146, 12);\n"
"    background-color: rgb(255, 146, 12);\n"
"    selection-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.menubar.setObjectName("menubar")
        self.menu_0 = QtWidgets.QMenu(self.menubar)
        self.menu_0.setStyleSheet("selection-background-color: rgb(255, 146, 12);")
        self.menu_0.setObjectName("menu_0")
        self.menuSave = QtWidgets.QMenu(self.menu_0)
        self.menuSave.setObjectName("menuSave")
        self.menu_1 = QtWidgets.QMenu(self.menubar)
        self.menu_1.setStyleSheet("selection-background-color: rgb(255, 146, 12);")
        self.menu_1.setObjectName("menu_1")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setStyleSheet("selection-background-color: rgb(255, 146, 12);")
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolBar.setFont(font)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionBreak = QtWidgets.QAction(MainWindow)
        self.actionBreak.setObjectName("actionBreak")
        self.menu_0.addAction(self.menuSave.menuAction())
        self.menu_1.addAction(self.actionBreak)
        self.menu_2.addAction(self.actionSettings)
        self.menubar.addAction(self.menu_0.menuAction())
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.tabWidget_left.setCurrentIndex(0)
        self.tabWidget_right.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.formGroupBox_tab_l.setTitle(_translate("MainWindow", "菜单"))
        self.pushButton_4.setText(_translate("MainWindow", "常用菜单"))
        self.formGroupBox_tab_r1_1.setTitle(_translate("MainWindow", "操作"))
        self.label.setText(_translate("MainWindow", "日期"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.pushButton_3.setText(_translate("MainWindow", "查询"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "新建行"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "表格"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "项目1"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "项目2"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "全部"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "项目1"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "子项目1"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "项目2"))
        self.treeWidget.topLevelItem(0).child(1).child(0).setText(0, _translate("MainWindow", "子项目2"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.formGroupBox_tab_r1_2.setTitle(_translate("MainWindow", "日志"))
        self.tabWidget_right.setTabText(self.tabWidget_right.indexOf(self.tab_r1), _translate("MainWindow", "page1"))
        self.tabWidget_right.setTabText(self.tabWidget_right.indexOf(self.tab_r2), _translate("MainWindow", "page2-middle"))
        self.tabWidget_right.setTabText(self.tabWidget_right.indexOf(self.tab_r3), _translate("MainWindow", "page3-very-very-long"))
        self.menu_0.setTitle(_translate("MainWindow", "首页"))
        self.menuSave.setTitle(_translate("MainWindow", "Home"))
        self.menu_1.setTitle(_translate("MainWindow", "功能"))
        self.menu_2.setTitle(_translate("MainWindow", "设置"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "Break"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit"))
        self.actionSettings.setText(_translate("MainWindow", "数据库管理"))
        self.actionSettings.setToolTip(_translate("MainWindow", "数据库管理"))
        self.actionBreak.setText(_translate("MainWindow", "数据拆分"))

