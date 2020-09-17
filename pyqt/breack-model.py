# -*- coding: utf-8 -*-

import time, datetime, re
from PyQt5 import QtCore, QtGui, QtWidgets, sip
##from mysql.models import User, Product, File
##import mysql.orm as orm
#from mysql.orm import create_pool, close_pool
##from mysql.config import configs
##import asyncio, threading
#import logging; logging.basicConfig(level=logging.INFO)
from excel import read_excel, PRODUCT_CATEGORY, PRODUCT_NAME, PRODUCT_SEND_PATH, PRODUCT_SEND_NAME, IF_UZIP
#from multiprocessing import Process, Pool, Manager, freeze_support
from send import send
from collections import defaultdict

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #############################################################################
        screen = QtWidgets.QDesktopWidget().screenGeometry() #frameGeometry()
        screen_width = screen.width()*0.8
        screen_height = screen.height()*0.8
        MainWindow.resize(screen_width, screen_height)
        # move方法含标题栏高度，setGeometry不含
        size = MainWindow.geometry() #获取不含标题栏rect
        MainWindow.setGeometry((screen.width() - size.width()) // 2,
                  (screen.height() - size.height()) // 2, screen_width, screen_height)
        '''
        mainframe = MainWindow.frameGeometry()
        screen_center = QtWidgets.QDesktopWidget().availableGeometry().center()
        mainframe.moveCenter(screen_center)
        MainWindow.move(mainframe.topLeft())
        '''
        #############################################################################
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("static/Mug-PNG.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        #MainWindow.setIconSize(QtCore.QSize(30, 30)) #设置了也不会改变大小
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        ###################################################################
        #选择窗口风格
        self.originalPalette = QtWidgets.QApplication.palette()
        self.styleComboBox = QtWidgets.QComboBox()
        self.styleComboBox.addItems(QtWidgets.QStyleFactory.keys())
        #print(QtWidgets.QStyleFactory.keys()) #支持的窗口风格
        self.styleComboBox.setCurrentIndex(QtWidgets.QStyleFactory.keys().index('Fusion'))
        self.styleComboBox.setDisabled(True)
        styleLabel = QtWidgets.QLabel("&窗口风格:")
        styleLabel.setBuddy(self.styleComboBox)
        self.useStylePaletteCheckBox = QtWidgets.QCheckBox("&单色调窗口")
        self.useStylePaletteCheckBox.setChecked(False)
        self.useStylePaletteCheckBox.setDisabled(True)
        self.disableWidgetsCheckBox = QtWidgets.QCheckBox("&锁定窗口")

        topLayout = QtWidgets.QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(self.styleComboBox)
        topLayout.addStretch(1)
        topLayout.addWidget(self.useStylePaletteCheckBox)
        topLayout.addWidget(self.disableWidgetsCheckBox)
        self.verticalLayout.addLayout(topLayout)

        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion')) #Fusion、Windows、windowsvista
        QtWidgets.QApplication.setPalette(QtWidgets.QApplication.style().standardPalette())
        ###################################################################

        ###################################################################
        #left-panel
        self.horizontalLayout_main = QtWidgets.QHBoxLayout()
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")
        self.formGroupBox_tab_l = QtWidgets.QGroupBox(self.centralwidget)
        self.formGroupBox_tab_l.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formGroupBox_tab_l.sizePolicy().hasHeightForWidth())
        self.formGroupBox_tab_l.setSizePolicy(sizePolicy)
        #font = QtGui.QFont()
        #font.setBold(True)
        #font.setWeight(75)
        #self.formGroupBox_tab_l.setFont(font)
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
            "    border-right: 3px solid rgb(211,211,211);\n"
            "}    \n"
            "QTabBar::tab:!selected {\n"
            "    margin-left: 0px;\n"
            "} \n"
            "QTabBar::tab:!selected:hover {\n"
                "border-right: 3px solid orange;\n"
                "border-top-left-radius: 0px;\n"
                "border-bottom-left-radius: 0px;\n"
            "}\n"
            "QTabBar::tab:selected {\n"
            "    background-color: white;\n"
            "    border-right: 3px solid green;\n"
            "    border-top-left-radius: 0px;\n"
            "    border-bottom-left-radius: 0px;\n"
            "}\n"
            "\n"
            " QTabWidget::tab-bar {\n"
            "     right: 0px; /* move to the right by 5px */\n"
            " }")
        self.tabWidget_left.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_left.setObjectName("tabWidget_left")
        self.tabWidget_left.setIconSize(QtCore.QSize(80, 20))
        self.tab_l1 = QtWidgets.QWidget()
        self.tab_l1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab_l1.setObjectName("tab_l1")
        self.horizontalLayout_tab_l1 = QtWidgets.QHBoxLayout(self.tab_l1)
        self.horizontalLayout_tab_l1.setContentsMargins(15, 15, 15, 5)
        self.horizontalLayout_tab_l1.setObjectName("horizontalLayout_tab_l1")
        self.frame_tab_l1 = QtWidgets.QFrame(self.tab_l1)
        self.frame_tab_l1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tab_l1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tab_l1.setObjectName("frame_tab_l1")
        self.verticalLayout_tab_l1 = QtWidgets.QVBoxLayout(self.frame_tab_l1)
        self.verticalLayout_tab_l1.setObjectName("verticalLayout_tab_l1")
        self.used_button1 = QtWidgets.QPushButton(self.frame_tab_l1)
        self.used_button1.setObjectName("used_button1")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.used_button1.sizePolicy().hasHeightForWidth())
        self.used_button1.setSizePolicy(sizePolicy)
        self.used_button1.setText("信托数据发送")
        self.used_button1.clicked.connect(self.addtab_right) #常用菜单信号处理函数
        self.verticalLayout_tab_l1.addWidget(self.used_button1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_tab_l1.addItem(spacerItem)
        self.horizontalLayout_tab_l1.addWidget(self.frame_tab_l1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("static/recent.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_left.addTab(self.tab_l1, icon, "")
        self.tab_l2 = QtWidgets.QWidget()
        self.tab_l2.setObjectName("tab_l2")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("static/star.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_left.addTab(self.tab_l2, icon1, "")
        self.horizontalLayout_left.addWidget(self.tabWidget_left)
        self.horizontalLayout_main.addWidget(self.formGroupBox_tab_l)
        ###################################################################

        ###################################################################
        #right-panel
        self.tabWidget_right = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_right.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_right.setFont(font)
        self.tabWidget_right.setStyleSheet("QTabBar::tab {\n"
            "    min-height:25px;\n"
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
                "border-bottom: 3px solid orange;\n"
                "border-top-left-radius: 0px;\n"
                "border-top-right-radius: 0px;\n"
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
            " }")
        self.tabWidget_right.setTabsClosable(True)
        self.tabWidget_right.tabCloseRequested.connect(self.closeTab) #关闭按钮事件
        self.tabWidget_right.tabBarDoubleClicked.connect(self.closeTab) #双击关闭事件
        self.tabWidget_right.setMovable(True)
        self.tabWidget_right.setObjectName("tabWidget_right")
        ###################################################################

        self.horizontalLayout_main.addWidget(self.tabWidget_right)
        self.horizontalLayout_main.setStretch(0, 1)
        self.horizontalLayout_main.setStretch(1, 5)
        
        self.verticalLayout.addLayout(self.horizontalLayout_main)
        MainWindow.setCentralWidget(self.centralwidget)

        ###################################################################
        #menu-tool
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("QMenuBar{\n"
            "    background-color: rgb(129, 198, 223);\n"
            "}\n"
            "QMenuBar:selected {\n"
            "    selection-background-color: rgb(255, 146, 12);\n"
            "    background-color: rgb(255, 146, 12);\n"
            "    selection-color: rgb(255, 255, 255);\n"
            "    color: rgb(255, 255, 255);\n"
            "}")
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
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
        font.setFamily("宋体")
        font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        self.toolBar.setFont(font)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('Exit')
        self.actionExit.triggered.connect(self.close)

        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionBreak = QtWidgets.QAction(MainWindow)
        self.actionBreak.setObjectName("actionBreak")
        self.actionBreak.triggered.connect(self.addtab_right)
        self.menu_0.addAction(self.menuSave.menuAction())
        self.menu_1.addAction(self.actionBreak)
        self.menu_2.addAction(self.actionSettings)
        self.menubar.addAction(self.menu_0.menuAction())
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)
        ###################################################################
        self.retranslateUi(MainWindow)
        self.tabWidget_left.setCurrentIndex(0)
        self.tabWidget_right.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.__signal_connect()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据拆分程序"))
        self.formGroupBox_tab_l.setTitle(_translate("MainWindow", "菜单"))
        #self.tabWidget_left.setTabText(self.tabWidget_left.indexOf(self.tab_l1), _translate("MainWindow", "常用菜单"))
        #self.tabWidget_left.setTabText(self.tabWidget_left.indexOf(self.tab_l2), _translate("MainWindow", "收藏"))
        '''
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "全部"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "项目1"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "子项目1"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "项目2"))
        self.treeWidget.topLevelItem(0).child(1).child(0).setText(0, _translate("MainWindow", "子项目2"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.formGroupBox_tab_r1_1.setTitle(_translate("MainWindow", "操作"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))
        self.formGroupBox_tab_r1_2.setTitle(_translate("MainWindow", "日志"))
        self.tabWidget_right.setTabText(self.tabWidget_right.indexOf(self.tab_r1), _translate("MainWindow", "page1"))
        #self.tabWidget_right.setTabText(self.tabWidget_right.indexOf(self.tab_r2), _translate("MainWindow", "page2-middle"))
        #self.tabWidget_right.setTabText(self.tabWidget_right.indexOf(self.tab_r3), _translate("MainWindow", "page3-very-very-long"))
        '''
        self.menu_0.setTitle(_translate("MainWindow", "首页"))
        self.menuSave.setTitle(_translate("MainWindow", "Home"))
        self.menu_1.setTitle(_translate("MainWindow", "功能"))
        self.menu_2.setTitle(_translate("MainWindow", "设置"))
        #self.toolBar.setWindowTitle(_translate("MainWindow", "ToolBarTitle"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit"))
        self.actionSettings.setText(_translate("MainWindow", "数据库管理"))
        self.actionSettings.setToolTip(_translate("MainWindow", "数据库管理"))
        self.actionBreak.setText(_translate("MainWindow", "信托数据发送"))

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.warning(self, '警告', '程序将终止运行,\n你确认要退出吗？',
                                           QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def changeStyle(self, styleName):
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(styleName))
        self.changePalette()

    def changePalette(self):
        if (self.useStylePaletteCheckBox.isChecked()):
            QtWidgets.QApplication.setPalette(QtWidgets.QApplication.style().standardPalette())
        else:
            QtWidgets.QApplication.setPalette(self.originalPalette)

    def closeTab(self, index):
        self.tabWidget_right.removeTab(index)

    def __signal_connect(self):
        self.styleComboBox.activated[str].connect(self.changeStyle)
        self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
        self.disableWidgetsCheckBox.toggled.connect(self.tabWidget_left.setDisabled)
        self.disableWidgetsCheckBox.toggled.connect(self.tabWidget_right.setDisabled)


class Model(QtWidgets.QMainWindow, Ui_MainWindow):
    EXIT_CODE_REBOOT = -123
    def __init__(self):
        super().__init__()
        self.file_path = 'products.xlsx'
        self.des_sort = True
        self.setupUi(self)
        self.retranslateUi(self)
        self.addtab_right()

    def moveEvent(self, event):
        x, y = event.pos().x(), event.pos().y()
        #print("x = {0}; y = {1}".format(x, y))
        QtWidgets.QMainWindow.moveEvent(self, event)
        if hasattr(self, 'the_dialog'):
            self.the_busydialog.move(x+(self.width()-self.the_busydialog.width())//2, y+(self.height()-self.the_busydialog.height())//2)
            #self.the_busydialog.raise_()
    '''
    def mousePressEvent(self,  event):
        if hasattr(self, 'the_dialog'):
            self.the_busydialog.raise_()
    def changeEvent(self, e):
        if e.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():
                print("窗口最小化")
            elif self.isMaximized():
                print("窗口最大化")
            elif self.isFullScreen():
                print("全屏显示")
            elif self.isActiveWindow():
                print("活动窗口")
        QtWidgets.QWidget.changeEvent(self, e)

    def resizeEvent(self, e):
        w, h = e.size().width(),e.size().height()
        #print("w = {0}; h = {1}".format(w, h))
        QtWidgets.QMainWindow.resizeEvent(self, e)
    '''
    def HorizontalHeaderClicked(self, index):
        #print(index)
        if int(index) == 0:
            self.tableWidget_tab_r1.setSortingEnabled(False)
        else:
            if self.des_sort == True:
                self.des_sort = False
                self.tableWidget_tab_r1.sortItems(index, QtCore.Qt.DescendingOrder)
            else:
                self.des_sort = True
                self.tableWidget_tab_r1.sortItems(index, QtCore.Qt.AscendingOrder)
            self.tableWidget_tab_r1.setSortingEnabled(True)
    
    def AdjustTableCellHeight(self, index):
        pass

    def addtab_right(self):  
        try:
            if self.tabWidget_right.tabText(self.tabWidget_right.indexOf(self.tab_r1)).strip().lower() == '信托数据发送':
                return 
        except:
            pass
        self.records = read_excel(cat=None, file_path=self.file_path)

        self.tab_r1 = QtWidgets.QWidget()
        self.tab_r1.setObjectName("tab_r1")
        gridLayout_tab_r1 = QtWidgets.QGridLayout(self.tab_r1)
        gridLayout_tab_r1.setContentsMargins(2, 2, 2, 2)
        gridLayout_tab_r1.setHorizontalSpacing(0)
        gridLayout_tab_r1.setObjectName("gridLayout_tab_r1")
        
        ##-----------------------------------------------------------------
        self.tableWidget_tab_r1 = QtWidgets.QTableWidget(self.tab_r1)       
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.tableWidget_tab_r1.setFont(font)
        self.tableWidget_tab_r1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_tab_r1.setStyleSheet("selection-background-color: rgb(255,165,0);selection-color: rgb(65,105,225);border-color: red;")
        self.tableWidget_tab_r1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        #self.tableWidget_tab_r1.setSortingEnabled(True)
        self.tableWidget_tab_r1.verticalHeader().setVisible(False)
        self.tableWidget_tab_r1.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_tab_r1.horizontalHeader().setHighlightSections(False) #取消表格头高亮
        self.tableWidget_tab_r1.horizontalHeader().sectionClicked.connect(self.HorizontalHeaderClicked)
        self.tableWidget_tab_r1.verticalHeader().setDefaultSectionSize(22)
        self.tableWidget_tab_r1.setObjectName("tableWidget_tab_r1") 

        HEADER_POS =      0
        COLUMN_SEND_PATH_POS =   PRODUCT_SEND_PATH + 1
        COLUMN_IF_UZIP = IF_UZIP + 1 
        
        column_name_list = ['选项'] + [rec.strip() for rec in self.records[HEADER_POS]] + ['处理状态']
        column_length = len(column_name_list)
        self.tableWidget_tab_r1.setColumnCount(column_length)
        for i in range(column_length):
            if i == HEADER_POS:
                self.tableWidget_tab_r1.setColumnWidth(HEADER_POS, 40)
                continue
            if i == COLUMN_SEND_PATH_POS:
                self.tableWidget_tab_r1.setColumnWidth(COLUMN_SEND_PATH_POS, 150)
                continue
            if i==1 or i==column_length-1 or i==COLUMN_IF_UZIP:
                self.tableWidget_tab_r1.setColumnWidth(i, 80)
                continue
            self.tableWidget_tab_r1.setColumnWidth(i, 250)
        self.tableWidget_tab_r1.setHorizontalHeaderLabels(column_name_list)  #设置列名称
        #self.tableWidget_tab_r1.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        
        self.tableWidget_tab_r1.setRowCount(len(self.records)-1)
        for i, record in enumerate(self.records[1:], 0):
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Checked)
            #self.tableWidget_tab_r1.setRowHeight(i, 25) #效果不好
            self.tableWidget_tab_r1.setItem(i, 0, item)
            for j, cell in  enumerate(record, 1):
                self.tableWidget_tab_r1.setItem(i, j, QtWidgets.QTableWidgetItem(cell))
                if j % COLUMN_SEND_PATH_POS == 0:
                    self.tableWidget_tab_r1.item(i, j).setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                    continue
                self.tableWidget_tab_r1.item(i, j).setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        #self.tableWidget_tab_r1.clear() #clearContents()
        #print(self.tableWidget_tab_r1.item(0, 0).checkState()) #获取选中状态
        #print(self.tableWidget_tab_r1.item(0, 1).text()) #获取选中状态
        #print(self.tableWidget_tab_r1.rowCount(), self.tableWidget_tab_r1.columnCount()) #获取表格行数

        #QtWidgets.QTableWidget.resizeColumnsToContents(self.tableWidget_tab_r1)
        #self.tableWidget_tab_r1.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        #self.tableWidget_tab_r1.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        #QtWidgets.QTableWidget.resizeRowsToContents(self.tableWidget_tab_r1) #放在设置内容后才生效
        #self.tableWidget_tab_r1.itemClicked.connect(self.AdjustTableCellHeight)      
        gridLayout_tab_r1.addWidget(self.tableWidget_tab_r1, 0, 1, 1, 1) #添加表格框架
        
        ##-----------------------------------------------------------------
        self.treeWidget_tab_r1 = QtWidgets.QTreeWidget(self.tab_r1)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.treeWidget_tab_r1.setFont(font)
        self.treeWidget_tab_r1.setStyleSheet("selection-background-color: rgb(255,165,0);selection-color: rgb(65,105,225);")
        self.treeWidget_tab_r1.setColumnCount(2)
        self.treeWidget_tab_r1.setObjectName("treeWidget")
        #self.treeWidget_tab_r1.headerItem().setText(0, "选项")
        #self.treeWidget_tab_r1.headerItem().setText(1, "名称")
        self.treeWidget_tab_r1.setHeaderLabels(["选项", "名称"])
        self.treeWidget_tab_r1.setColumnWidth(0, 250)
        self.root_tab_r1 = QtWidgets.QTreeWidgetItem(self.treeWidget_tab_r1)
        self.root_tab_r1.setCheckState(0, QtCore.Qt.Checked)
        self.item_c1_1 = QtWidgets.QTreeWidgetItem(self.root_tab_r1)
        self.item_c1_1.setCheckState(0, QtCore.Qt.Checked)
        #print(self.item_c1_1.child(0).text(0))
        item_c21_1 = QtWidgets.QTreeWidgetItem(self.item_c1_1)
        item_c21_1.setCheckState(0, QtCore.Qt.Checked)
        #item_c21_2 = QtWidgets.QTreeWidgetItem(self.item_c1_1)
        #item_c21_2.setCheckState(0, QtCore.Qt.Checked)
        self.item_c1_2 = QtWidgets.QTreeWidgetItem(self.root_tab_r1)
        self.item_c1_2.setCheckState(0, QtCore.Qt.Checked)
        item_c22_1 = QtWidgets.QTreeWidgetItem(self.item_c1_2)
        item_c22_1.setCheckState(0, QtCore.Qt.Checked)
        self.treeWidget_tab_r1.topLevelItem(0).setText(0, "全部")
        self.treeWidget_tab_r1.topLevelItem(0).child(0).setText(0, "普通交易")
        self.treeWidget_tab_r1.topLevelItem(0).child(0).child(0).setText(0, "第一批数据")
        #self.treeWidget_tab_r1.topLevelItem(0).child(0).child(1).setText(0, "资管数据拆分")
        self.treeWidget_tab_r1.topLevelItem(0).child(1).setText(0, "融资融券")
        self.treeWidget_tab_r1.topLevelItem(0).child(1).child(0).setText(0, "清算后数据")
        #__sortingEnabled = self.treeWidget_tab_r1.isSortingEnabled()
        self.treeWidget_tab_r1.setSortingEnabled(False)
        #self.treeWidget_tab_r1.setSortingEnabled(__sortingEnabled)
        self.treeWidget_tab_r1.expandAll() #放在末尾才能生效 expandItem()、collapseItem()函数分别展开、收起指定节点
        self.treeWidget_tab_r1.itemClicked.connect(self.treeChecked) #itemChanged
        gridLayout_tab_r1.addWidget(self.treeWidget_tab_r1, 0, 0, 1, 1) #添加树形选择框架

        ##-----------------------------------------------------------------
        formGroupBox_tab_r1_1 = QtWidgets.QGroupBox(self.tab_r1)
        formGroupBox_tab_r1_1.setObjectName("formGroupBox_tab_r1_1")
        formGroupBox_tab_r1_1.setTitle("操作")
        horizontalLayout_middle = QtWidgets.QHBoxLayout(formGroupBox_tab_r1_1)
        horizontalLayout_middle.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_middle.setObjectName("horizontalLayout_middle")
        
        label = QtWidgets.QLabel(formGroupBox_tab_r1_1)
        label.setObjectName("label")
        label.setText("日期")
        horizontalLayout_middle.addWidget(label)
        self.dateEdit_tab_r1 = QtWidgets.QDateEdit(formGroupBox_tab_r1_1)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.dateEdit_tab_r1.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_tab_r1.sizePolicy().hasHeightForWidth())
        self.dateEdit_tab_r1.setCalendarPopup(True)
        self.dateEdit_tab_r1.setObjectName("dateEdit_tab_r1")
        self.dateEdit_tab_r1.setDisplayFormat("yyyy/MM/dd")
        self.dateEdit_tab_r1.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_tab_r1.setMinimumSize(QtCore.QSize(150, 0))
        #print(self.dateEdit_tab_r1.text()) #获取日期
        horizontalLayout_middle.addWidget(self.dateEdit_tab_r1)
        self.lineEdit_tab_r1 = QtWidgets.QLineEdit(formGroupBox_tab_r1_1)
        self.lineEdit_tab_r1.setObjectName("lineEdit")
        horizontalLayout_middle.addWidget(self.lineEdit_tab_r1)
        pushButton_3 = QtWidgets.QPushButton(formGroupBox_tab_r1_1)
        pushButton_3.setObjectName("pushButton_3")
        pushButton_3.setText("查询")
        pushButton_3.clicked.connect(self.do_pushButton_tab_r1_3)
        horizontalLayout_middle.addWidget(pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        horizontalLayout_middle.addItem(spacerItem)
        
        self.pushButton = QtWidgets.QPushButton(formGroupBox_tab_r1_1)
        self.pushButton.setText("确定")
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.do_pushButton_tab_r1_1)
        horizontalLayout_middle.addWidget(self.pushButton)
        pushButton_2 = QtWidgets.QPushButton(formGroupBox_tab_r1_1)
        pushButton_2.setText("取消")
        pushButton_2.setObjectName("pushButton_2")
        pushButton_2.clicked.connect(self.do_pushButton_tab_r1_2)
        horizontalLayout_middle.addWidget(pushButton_2)
        gridLayout_tab_r1.addWidget(formGroupBox_tab_r1_1, 1, 0, 1, 2) #添加操作按钮框架

        ##-----------------------------------------------------------------
        formGroupBox_tab_r1_2 = QtWidgets.QGroupBox(self.tab_r1)
        formGroupBox_tab_r1_2.setObjectName("formGroupBox_tab_r1_2")
        formGroupBox_tab_r1_2.setTitle("日志")
        horizontalLayout_bottom = QtWidgets.QHBoxLayout(formGroupBox_tab_r1_2)
        horizontalLayout_bottom.setContentsMargins(2, 2, 2, 2)
        horizontalLayout_bottom.setObjectName("horizontalLayout_bottom")
        self.textEdit_tab_r1 = QtWidgets.QTextEdit(formGroupBox_tab_r1_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.textEdit_tab_r1.setFont(font)
        self.textEdit_tab_r1.setReadOnly(True)
        self.textEdit_tab_r1.setObjectName("textEdit_tab_r1")
        #self.textEdit_tab_r1.setHtml("<font color='red' size='2'>[2019/08/30:12]第一条日志<br>换行<br></font>")
        #self.textEdit_tab_r1.append("<font color='black' size='2'>[2019/08/30:45]第二条日志</font>")
        #self.textEdit_tab_r1.moveCursor(QtGui.QTextCursor.End)
        #self.textEdit_tab_r1.insertPlainText("\n追加内容") #追加到现有内容后面
        #print(self.textEdit_tab_r1.toPlainText())
        horizontalLayout_bottom.addWidget(self.textEdit_tab_r1)
        gridLayout_tab_r1.addWidget(formGroupBox_tab_r1_2, 2, 0, 1, 2) #添加日志框架

        ##-----------------------------------------------------------------
        self.progressBar_tab_r1 = QtWidgets.QProgressBar(self.tab_r1)
        self.progressBar_tab_r1.setStyleSheet('text-align:center;color:rgb(255, 255, 255)')
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.progressBar_tab_r1.setFont(font)
        #self.progressBar_tab_r1.setProperty("value", 0)
        #self.progressBar_tab_r1.setRange(0, 10000)
        self.progressBar_tab_r1.setValue(0)
        #timer = QtCore.QTimer(self) #Qtimer为一个多线程计时器，timeout触发事件
        #timer.timeout.connect(self.advanceProgressBar)
        #timer.start(1000)
        self.progressBar_tab_r1.setObjectName("progressBar_tab_r1")
        gridLayout_tab_r1.addWidget(self.progressBar_tab_r1, 3, 0, 1, 2) #添加进度条框架

        ##-----------------------------------------------------------------
        gridLayout_tab_r1.setColumnStretch(1, 4)
        gridLayout_tab_r1.setColumnStretch(0, 1)
        gridLayout_tab_r1.setRowStretch(2, 2)
        gridLayout_tab_r1.setRowStretch(0, 5)
        self.tabWidget_right.addTab(self.tab_r1, "")
        self.tabWidget_right.setTabText(self.tabWidget_right.indexOf(self.tab_r1), "信托数据发送")
        self.tabWidget_right.setCurrentWidget(self.tab_r1) 
    
    def advanceProgressBar(self):
        '''
        curVal = self.progressBar_tab_r1.value()
        maxVal = self.progressBar_tab_r1.maximum()
        val = curVal + max((maxVal - curVal) / 10, 10)
        if val <= maxVal:
            self.progressBar_tab_r1.setValue(val)
            curVal = val 
        else:
            self.progressBar_tab_r1.setValue(maxVal)
        '''
        self.progressBar_tab_r1.setValue(0)

    def treeChecked(self, item, column):

        def __forwardcheck(item, column):
            child_counts = item.childCount()
            if item.checkState(column) == QtCore.Qt.Checked:
                #print("checked", item, item.text(column))
                for f in range(child_counts):
                    item.child(f).setCheckState(0, QtCore.Qt.Checked)
            if item.checkState(column) == QtCore.Qt.Unchecked:
                for f in range(child_counts):
                    item.child(f).setCheckState(0, QtCore.Qt.Unchecked)

        def __backcheck(item, column):
            parent_item = item.parent()
            if item.checkState(column) == QtCore.Qt.Checked:
                parent_child_counts = parent_item.childCount()
                allchecked = 1
                for f in range(parent_child_counts):
                    if parent_item.child(f).checkState(column) == QtCore.Qt.Unchecked:
                        allchecked = 0
                        break
                if allchecked:
                    parent_item.setCheckState(0, QtCore.Qt.Checked)
            else:
                parent_item.setCheckState(0, QtCore.Qt.Unchecked)
        if item == self.root_tab_r1:
            __forwardcheck(item, column)
            child_counts = item.childCount()
            for n in range(child_counts):
                child_item = item.child(n)
                __forwardcheck(child_item, column)
        elif item == self.item_c1_1 or item == self.item_c1_2:
            __forwardcheck(item, column)
            __backcheck(item, column)
        else:
            __backcheck(item, column)
            parent_item = item.parent()
            __backcheck(parent_item, column)

        rows = self.tableWidget_tab_r1.rowCount()
        cols = self.tableWidget_tab_r1.columnCount()
        '''
        if self.root_tab_r1.checkState(column) == QtCore.Qt.Checked:
            for row in range(rows):
                item = QtWidgets.QTableWidgetItem()
                item.setCheckState(QtCore.Qt.Checked)
                self.tableWidget_tab_r1.setItem(row, 0, item)
        '''
        if self.item_c1_1.checkState(column) == QtCore.Qt.Checked:
            for row in range(rows):
                if self.tableWidget_tab_r1.item(row, 1) and self.tableWidget_tab_r1.item(row, 1).text() == self.item_c1_1.child(0).text(0)[0:3]:
                    item = QtWidgets.QTableWidgetItem()
                    item.setCheckState(QtCore.Qt.Checked)
                    self.tableWidget_tab_r1.setItem(row, 0, item)
        else:
            for row in range(rows):
                if self.tableWidget_tab_r1.item(row, 1) and  self.tableWidget_tab_r1.item(row, 1).text() == self.item_c1_1.child(0).text(0)[0:3]:
                    item = QtWidgets.QTableWidgetItem()
                    item.setCheckState(QtCore.Qt.Unchecked)
                    self.tableWidget_tab_r1.setItem(row, 0, item)
        if self.item_c1_2.checkState(column) == QtCore.Qt.Checked:
            for row in range(rows):
                if self.tableWidget_tab_r1.item(row, 1) and self.tableWidget_tab_r1.item(row, 1).text() == self.item_c1_2.child(0).text(0)[0:3]:
                    item = QtWidgets.QTableWidgetItem()
                    item.setCheckState(QtCore.Qt.Checked)
                    self.tableWidget_tab_r1.setItem(row, 0, item)
        else:
            for row in range(rows):
                if self.tableWidget_tab_r1.item(row, 1) and self.tableWidget_tab_r1.item(row, 1).text() == self.item_c1_2.child(0).text(0)[0:3]:
                    item = QtWidgets.QTableWidgetItem()
                    item.setCheckState(QtCore.Qt.Unchecked)
                    self.tableWidget_tab_r1.setItem(row, 0, item)
    
    def do_pushButton_tab_r1_1(self, event):
        reply = QtWidgets.QMessageBox.warning(self, '警告', '确定开始发送信托数据？',
                                           QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.No:
            return
        self.pushButton.setDisabled(True)
        self.tableWidget_tab_r1.setSortingEnabled(False)
        self.the_busydialog = BusyDialog('程序正在运行，请稍候...')
        self.the_busydialog.move(self.geometry().left()+(self.width()-self.the_busydialog.width())//2, self.geometry().top()+(self.height()-self.the_busydialog.height())//2)
        thread = SendData(self)
        thread.start()
        thread.progress_trigger.connect(self.advanceProgressBar)
        thread.update_triger.connect(self.update_table_tabr1)
        thread.trigger.connect(self.finish)
        self.the_busydialog.exec_()
        self.pushButton.setDisabled(False)
        #self.tableWidget_tab_r1.setSortingEnabled(True)
        '''
        ####################################################################
        self.the_busydialog = BusyDialog('程序正在运行，请稍候...')
        self.the_busydialog.move(self.geometry().left()+(self.width()-self.the_busydialog.width())//2, self.geometry().top()+(self.height()-self.the_busydialog.height())//2)
        #self.setDisabled(True)
        #the_dialog.show()
        thread = BreackThread(self.tableWidget_tab_r1)
        #thread = BreackThread()
        thread.start()
        thread.update_triger.connect(self.update_table_tabr1)
        thread.trigger.connect(self.finish)
        #QtWidgets.qApp.processEvents()
        #self.the_busydialog.setWindowModality(QtCore.Qt.NonModal) #WindowModal、ApplicationModal、NonModal
        self.the_busydialog.exec_()
        #self.raise_()
        #if self.the_busydialog.exec_() == QtWidgets.QDialog.Accepted:
        #    pass
        ####################################################################
        '''
    def do_pushButton_tab_r1_2(self, event):
        self.tabWidget_right.removeTab(self.tabWidget_right.indexOf(self.tab_r1))
        '''
        ####################################################################
        self.the_busydialog = BusyDialog('正在访问数据库，请勿退出程序...')
        self.the_busydialog.move(self.geometry().left()+(self.width()-self.the_busydialog.width())//2, self.geometry().top()+(self.height()-self.the_busydialog.height())//2)
        thread = Register()
        thread.start()
        thread.trigger.connect(self.finish)
        self.the_busydialog.exec_()
        ####################################################################
        '''
    def do_pushButton_tab_r1_3(self, event):
        self.tableWidget_tab_r1.setSortingEnabled(False)
        
        search_list = list(filter(None, re.split(" |,|，|;|；", self.lineEdit_tab_r1.text()) ))

        isflush = False
        if not search_list:
            records = read_excel(cat=None, file_path="products.xlsx")
            isflush = True

        #self.tableWidget_tab_r1.hideRow(0)
        self.tableWidget_tab_r1.clearContents()
        self.tableWidget_tab_r1.setRowCount(0)

        if (not isflush) and search_list:
            records = [[],]
            for ser in search_list:
                for record in self.records[1:]:
                    if ser in "".join([rec for rec in record if rec]):
                        records.append(record)

        self.tableWidget_tab_r1.setRowCount(len(records)-1)
        for i, record in enumerate(records[1:], 0):
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Checked)
            self.tableWidget_tab_r1.setItem(i, 0, item)
            #self.tableWidget_tab_r1.setRowHeight(i, 25)
            for j, cell in  enumerate(record, 1):
                self.tableWidget_tab_r1.setItem(i, j, QtWidgets.QTableWidgetItem(cell))
                if j % 3 == 0:
                    self.tableWidget_tab_r1.item(i, j).setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                    continue
                self.tableWidget_tab_r1.item(i, j).setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        '''
        for row in range(rows):
            record = [self.tableWidget_tab_r1.item(row, col).text() for col in range(1, cols-1)]
            print(record)
        '''

    def update_table_tabr1(self, data):
        pos = data[:2]
        today = data[2]
        value = data[3][1]
        tasks_num = data[4]
        if self.progressBar_tab_r1.value() == 0:
            self.progressBar_tab_r1.setRange(0, tasks_num)
        self.progressBar_tab_r1.setValue(self.progressBar_tab_r1.value()+1)
        res_state = data[-1]
        if res_state:
            message = "<font color='black' size='2'>"+str(today)+": 信托产品【"+value+"】 发送成功</font>"
            self.tableWidget_tab_r1.setItem(*pos, QtWidgets.QTableWidgetItem('发送成功'))
            self.tableWidget_tab_r1.item(*pos).setForeground(QtGui.QBrush(QtGui.QColor(0,0,0)))
        else:
            message = "<font color='red' size='2'>"+str(today)+": 信托产品【"+value+"】 发送失败</font>"            
            self.tableWidget_tab_r1.setItem(*pos, QtWidgets.QTableWidgetItem('发送失败'))
            self.tableWidget_tab_r1.item(*pos).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0))) #设置单元格字体颜色为红色  
        self.tableWidget_tab_r1.item(*pos).setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.textEdit_tab_r1.append(message)
        self.textEdit_tab_r1.moveCursor(QtGui.QTextCursor.End)

    def addtab_right_else():
        pass
        '''
        self.tab_r2 = QtWidgets.QWidget()
        self.tab_r2.setObjectName("tab_r2")
        self.tabWidget_right.setTabText(self.tabWidget_right.indexOf(self.tab_r2), "page2-middle")
        self.tabWidget_right.addTab(self.tab_r2, "")
        self.tab_r3 = QtWidgets.QWidget()
        self.tab_r3.setObjectName("tab_r3")
        self.tabWidget_right.addTab(self.tab_r3, "")
        #self.tabWidget_right.setTabText(self.tabWidget_right.indexOf(self.tab_r3), "page3-very-very-long")
        '''
    def finish(self):
        reply = QtWidgets.QMessageBox()
        #reply.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.the_busydialog.close()
        #self.the_busydialog.move(100,100)
        reply.information(self, "提示", "任务处理完成", QtWidgets.QMessageBox.Ok) #QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        #self.setEnabled(True)

    def load_data(self, sp):
        for i in range(1, 11):  # 模拟主程序加载过程
            time.sleep(0.1)     # 加载数据
            sp.showMessage("加载... {0}%".format(i * 10), QtCore.Qt.AlignCenter, QtCore.Qt.black)
            QtWidgets.qApp.processEvents()  # 允许主进程处理事件

class SendData(QtCore.QThread):
    trigger = QtCore.pyqtSignal()
    update_triger = QtCore.pyqtSignal(tuple)
    progress_trigger = QtCore.pyqtSignal()
    def __init__(self, obj, parent=None):
        super(SendData, self).__init__()
        self.obj = obj

    def __del__(self):
        self.wait()
    def run(self):
        self.progress_trigger.emit()
        '''
        pool = Pool(4)
        queue = Manager().Queue()

        def callback(results):
            for res in results:
                queue.put(res)
        '''
        
        rows = self.obj.tableWidget_tab_r1.rowCount()
        cols = self.obj.tableWidget_tab_r1.columnCount()
        break_time = ''.join(self.obj.dateEdit_tab_r1.text().split('/'))
        today = datetime.date.today()
        date = time.strftime('%Y-%m-%d %H:%M:%S')

        fp = open("log"+str(today)+".txt", "a")

        records = []
        for row in range(rows):
            record = [self.obj.tableWidget_tab_r1.item(row, col).text() for col in range(1, cols-1)]
            records.append(record)

        indexs = list([record[0:3] for record in records]) #产品名称位置索引

        tasks = defaultdict(list)
        queue_size = 0
        for n, rec in enumerate(records):
            if self.obj.tableWidget_tab_r1.item(n, 0).checkState() == QtCore.Qt.Checked:
                tasks[rec[2]].append(rec)
                queue_size += 1
                  
        tasks = list(tasks.values())
        '''
        thread_nums = len(tasks)
        for t in range(thread_nums):
            pool.apply_async(send, args=(tasks[t], break_time), kwds={}, callback=callback)

        done_num = 0
        while done_num < queue_size:
            value, res_state = queue.get(True)
            done_num += 1
            fp.write(date+" "+" ".join(value)+" "+str(res_state)+"\n")
            self.update_triger.emit((indexs.index(value), cols-1, date, value, queue_size, res_state))
            #print('产品【%s】处理完成' % value)
        
        pool.close()
        pool.join()
        pool.terminate()
        '''
        for t in tasks:
            results = send(t, break_time)
            for r in results:
                value, res_state = r
                fp.write(date+" "+" ".join(value)+" "+str(res_state)+"\n")
                self.update_triger.emit((indexs.index(value), cols-1, date, value, queue_size, res_state))
                #print('产品【%s】处理完成' % value)
        fp.close()
        
        self.trigger.emit()

'''
##########################################################################################
class BreackThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal()
    update_triger = QtCore.pyqtSignal(tuple)

    def __init__(self, table, parent=None):
        super(BreackThread, self).__init__()
        self.table = table

    def __del__(self):
        self.wait()

    def run(self):
        from dbf.dbf import DbfBreak
        from multiprocessing import Process, Pool, Manager
        pool = Pool(4)
        queue = Manager().Queue()

        def callback(res):
            queue.put(res)

        file_path = r'dbf/SJSGB.dbf'
        print('开始加载数据')
        res = DbfBreak(file_path)
        print('加载数据完成')

        rows = self.table.rowCount()
        cols = self.table.columnCount()

        for row in range(rows):
            pool.apply_async(res.Break, args=('dbf/file/breack'+str(row)+'.dbf',), kwds={'gbrq1':None, 'gbje1':0}, callback=callback)
        
        done_num = []
        while len(done_num) < rows:
            value = queue.get(True)
            done_num.append(value)
            self.update_triger.emit((int(value.split('.')[0][-1:]), 4, QtWidgets.QTableWidgetItem('已处理')))
            print('File %s has done.' % value)
        
        pool.close()
        pool.join()
        pool.terminate()

        
        #for row in range(rows):
        #    for col in range(1, cols):
        #        if col == cols-1:
        #            res.Break('dbf/file/breack'+str(row)+'.dbf', gbrq1=None, gbje1=0)
        #            self.update_triger.emit((row, col, QtWidgets.QTableWidgetItem('已处理')))
        
        self.trigger.emit()
##########################################################################################
'''

'''
##########################################################################################
#访问数据库模块
class SQLThread(QtCore.QObject):
    trigger = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(SQLThread, self).__init__(parent)

    def thread_asyncio_task(self, thread_loop, sqlcommand):
        asyncio.set_event_loop(thread_loop) 
        async def register():
            #await asyncio.sleep(5) #延迟测试
            await orm.create_pool(loop=thread_loop, **configs.db)
            if sqlcommand:
                await sqlcommand()
            #user = User(name='zengyongs', passwd='123456')
            #await user.save()
            await orm.close_pool()
            self.trigger.emit()
        future = asyncio.gather(register(),)
        thread_loop.run_until_complete(future)
        self.thread_loop.close()
        SQLThread.stop_thread(self.t)

    def run(self, sqlcommand=None):
        # 创建一个事件循环thread_loop
        self.thread_loop = asyncio.new_event_loop() 
        # 将thread_loop作为参数传递给子线程
        self.t = threading.Thread(target=self.thread_asyncio_task, args=(self.thread_loop, sqlcommand))
        self.t.setDaemon(True) #t.daemon==True 若设置为守护线程，主线程退出则子线程也退出。反之，则等待子线程完成再退出
        self.t.start()

    @staticmethod
    def _async_raise(tid, exctype):
        import inspect
        import ctypes
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
    @staticmethod
    def stop_thread(thread):
        SQLThread._async_raise(thread.ident, SystemExit)

class Register:
    @staticmethod
    async def sqlcommand():
        user = User(name='zengyongs', passwd='123456')
        await user.save()
    def start(self):
        t = SQLThread()
        self.trigger = t.trigger
        t.run(Register.sqlcommand)
##########################################################################################
'''

class BusyDialog(QtWidgets.QDialog):
    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self, text)
    def setupUi(self, Dialog, text): 
        #设置对话框类型
        #Dialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint|QtCore.Qt.FramelessWindowHint)
        #Dialog.setWindowFlags(QtCore.Qt.ToolTip|QtCore.Qt.FramelessWindowHint)
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.Tool) #|QtCore.Qt.WindowStaysOnTopHint导致切换窗口程序也总是位于窗口前面
        Dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground, False) #窗口是否透明
        Dialog.setObjectName("Dialog") 
        Dialog.resize(300, 100) 
        Dialog.setStyleSheet('background-color: white;')
        gridLayout = QtWidgets.QGridLayout(Dialog) 
        gridLayout.setObjectName("gridLayout") 
        self.progressBar_busy = QtWidgets.QProgressBar(Dialog) 
        #self.progressBar_busy.setProperty("value", 0) 
        self.progressBar_busy.setMinimum(0)
        self.progressBar_busy.setMaximum(0)
        self.progressBar_busy.setStyleSheet('QProgressBar{border-color: rgb(255, 255, 255);background-color:transparent;}QProgressBar::chunk{background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 orange,stop:1 red);}')
        self.progressBar_busy.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter) 
        self.progressBar_busy.setObjectName("progressBar_busy") 
        gridLayout.addWidget(self.progressBar_busy, 1, 0, 1, 1) 
        label_busy = QtWidgets.QLabel(Dialog) 
        label_busy.setObjectName("label_busy")  
        label_busy.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        label_busy.setText(text)
        gridLayout.addWidget(label_busy, 0, 0, 1, 1) 
      
        self.retranslateUi(Dialog) 
        QtCore.QMetaObject.connectSlotsByName(Dialog) 
  
    def retranslateUi(self, Dialog): 
        _translate = QtCore.QCoreApplication.translate 
        Dialog.setWindowTitle(_translate("Dialog", "BusyDialog")) 

if __name__ == "__main__":
    import sys
    #freeze_support()
    currentExitCode = Model.EXIT_CODE_REBOOT
    while currentExitCode == Model.EXIT_CODE_REBOOT:
        app = QtWidgets.QApplication(sys.argv)
        splash = QtWidgets.QSplashScreen(QtGui.QPixmap("static/start.png")) #QtGui.QPixmap("static/start.png"
        #splash.setStyleSheet('background-image: url(static/home.gif);')
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        splash.setFont(font)
        splash.showMessage("正在加载... 0%", QtCore.Qt.AlignCenter, QtCore.Qt.black) #QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom
        splash.show()                           # 显示启动界面
        QtWidgets.qApp.processEvents()          # 处理主进程事件
        w = Model()
        #w.showFullScreen() #全屏显示
        w.load_data(splash) 
        w.show()
        #w.setDisabled(True)
        splash.finish(w) 
        currentExitCode = app.exec_()
        app=None
        #sys.exit(app.exec_())
