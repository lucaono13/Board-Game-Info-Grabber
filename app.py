# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_run2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(929, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_4.addWidget(self.searchButton, 0, 2, 1, 1)
        self.searchLine = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLine.setClearButtonEnabled(False)
        self.searchLine.setObjectName("searchLine")
        self.gridLayout_4.addWidget(self.searchLine, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.gameCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.gameCheck.setObjectName("gameCheck")
        self.gridLayout_4.addWidget(self.gameCheck, 1, 0, 1, 1)
        self.expanCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.expanCheck.setChecked(False)
        self.expanCheck.setObjectName("expanCheck")
        self.gridLayout_4.addWidget(self.expanCheck, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.bgg_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.bgg_tabs.setEnabled(True)
        self.bgg_tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.bgg_tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.bgg_tabs.setIconSize(QtCore.QSize(16, 16))
        self.bgg_tabs.setTabBarAutoHide(False)
        self.bgg_tabs.setObjectName("bgg_tabs")
        self.bgg_search_tab = QtWidgets.QWidget()
        self.bgg_search_tab.setObjectName("bgg_search_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.bgg_search_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.addButton = QtWidgets.QPushButton(self.bgg_search_tab)
        self.addButton.setObjectName("addButton")
        self.gridLayout_3.addWidget(self.addButton, 0, 0, 1, 1)
        self.removeButton = QtWidgets.QPushButton(self.bgg_search_tab)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout_3.addWidget(self.removeButton, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.searchResults = QtWidgets.QTableWidget(self.bgg_search_tab)
        self.searchResults.setAlternatingRowColors(True)
        self.searchResults.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.searchResults.setGridStyle(QtCore.Qt.SolidLine)
        self.searchResults.setObjectName("searchResults")
        self.searchResults.setColumnCount(0)
        self.searchResults.setRowCount(0)
        self.searchResults.horizontalHeader().setSortIndicatorShown(True)
        self.gridLayout_2.addWidget(self.searchResults, 0, 0, 1, 1)
        self.bgg_tabs.addTab(self.bgg_search_tab, "")
        self.csv_edit = QtWidgets.QWidget()
        self.csv_edit.setObjectName("csv_edit")
        self.bgg_tabs.addTab(self.csv_edit, "")
        self.csvPreview = QtWidgets.QWidget()
        self.csvPreview.setObjectName("csvPreview")
        self.bgg_tabs.addTab(self.csvPreview, "")
        self.gridLayout.addWidget(self.bgg_tabs, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 929, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.bgg_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.searchLine, self.searchButton)
        MainWindow.setTabOrder(self.searchButton, self.gameCheck)
        MainWindow.setTabOrder(self.gameCheck, self.expanCheck)
        MainWindow.setTabOrder(self.expanCheck, self.bgg_tabs)
        MainWindow.setTabOrder(self.bgg_tabs, self.searchResults)
        MainWindow.setTabOrder(self.searchResults, self.addButton)
        MainWindow.setTabOrder(self.addButton, self.removeButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Board Game Name"))
        self.gameCheck.setText(_translate("MainWindow", "Game"))
        self.expanCheck.setText(_translate("MainWindow", "Expansion"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.searchResults.setSortingEnabled(True)
        self.bgg_tabs.setTabText(self.bgg_tabs.indexOf(self.bgg_search_tab), _translate("MainWindow", "BGG Search"))
        self.bgg_tabs.setTabToolTip(self.bgg_tabs.indexOf(self.bgg_search_tab), _translate("MainWindow", "Search Board Game Geek"))
        self.bgg_tabs.setTabText(self.bgg_tabs.indexOf(self.csv_edit), _translate("MainWindow", "CSV Edit"))
        self.bgg_tabs.setTabText(self.bgg_tabs.indexOf(self.csvPreview), _translate("MainWindow", "CSV Preview"))
