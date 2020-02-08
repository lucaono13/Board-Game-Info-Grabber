# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(679, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.searchLine = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLine.setClearButtonEnabled(False)
        self.searchLine.setObjectName("searchLine")
        self.gridLayout_4.addWidget(self.searchLine, 0, 1, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_4.addWidget(self.searchButton, 0, 2, 1, 1)
        self.expanCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.expanCheck.setChecked(False)
        self.expanCheck.setObjectName("expanCheck")
        self.gridLayout_4.addWidget(self.expanCheck, 1, 1, 1, 1)
        self.gameCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.gameCheck.setObjectName("gameCheck")
        self.gridLayout_4.addWidget(self.gameCheck, 1, 0, 1, 1)
        self.csvImport = QtWidgets.QPushButton(self.centralwidget)
        self.csvImport.setObjectName("csvImport")
        self.gridLayout_4.addWidget(self.csvImport, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.bgg_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.bgg_tabs.setEnabled(True)
        self.bgg_tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.bgg_tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.bgg_tabs.setIconSize(QtCore.QSize(16, 16))
        self.bgg_tabs.setDocumentMode(False)
        self.bgg_tabs.setTabBarAutoHide(False)
        self.bgg_tabs.setObjectName("bgg_tabs")
        self.bgg_search_tab = QtWidgets.QWidget()
        self.bgg_search_tab.setObjectName("bgg_search_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.bgg_search_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.searchResults = QtWidgets.QTableWidget(self.bgg_search_tab)
        self.searchResults.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.searchResults.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.searchResults.setAlternatingRowColors(True)
        self.searchResults.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.searchResults.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.searchResults.setGridStyle(QtCore.Qt.SolidLine)
        self.searchResults.setObjectName("searchResults")
        self.searchResults.setColumnCount(0)
        self.searchResults.setRowCount(0)
        self.searchResults.horizontalHeader().setSortIndicatorShown(True)
        self.gridLayout_2.addWidget(self.searchResults, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.addButton = QtWidgets.QPushButton(self.bgg_search_tab)
        self.addButton.setObjectName("addButton")
        self.gridLayout_3.addWidget(self.addButton, 0, 0, 1, 1)
        self.removeButton = QtWidgets.QPushButton(self.bgg_search_tab)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout_3.addWidget(self.removeButton, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.bgg_search_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 4, 0, 1, 1)
        self.selectedGamees = QtWidgets.QListWidget(self.bgg_search_tab)
        self.selectedGamees.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.selectedGamees.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.selectedGamees.setObjectName("selectedGamees")
        self.gridLayout_3.addWidget(self.selectedGamees, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.bgg_search_tab)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 7, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(15, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.dataCollectionStart = QtWidgets.QPushButton(self.bgg_search_tab)
        self.dataCollectionStart.setEnabled(False)
        self.dataCollectionStart.setObjectName("dataCollectionStart")
        self.gridLayout_3.addWidget(self.dataCollectionStart, 8, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 20)
        self.gridLayout_2.setColumnStretch(1, 5)
        self.bgg_tabs.addTab(self.bgg_search_tab, "")
        self.csvPreview = QtWidgets.QWidget()
        self.csvPreview.setEnabled(False)
        self.csvPreview.setObjectName("csvPreview")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.csvPreview)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.removeRow = QtWidgets.QPushButton(self.csvPreview)
        self.removeRow.setObjectName("removeRow")
        self.verticalLayout_2.addWidget(self.removeRow)
        self.exportButton = QtWidgets.QPushButton(self.csvPreview)
        self.exportButton.setObjectName("exportButton")
        self.verticalLayout_2.addWidget(self.exportButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout_7.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.dfPreview = QtWidgets.QTableView(self.csvPreview)
        self.dfPreview.setAlternatingRowColors(True)
        self.dfPreview.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.dfPreview.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.dfPreview.setObjectName("dfPreview")
        self.gridLayout_7.addWidget(self.dfPreview, 2, 0, 1, 1)
        self.bgg_tabs.addTab(self.csvPreview, "")
        self.csv_edit = QtWidgets.QWidget()
        self.csv_edit.setObjectName("csv_edit")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.csv_edit)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tableView = QtWidgets.QTableView(self.csv_edit)
        self.tableView.setObjectName("tableView")
        self.gridLayout_6.addWidget(self.tableView, 0, 0, 1, 1)
        self.bgg_tabs.addTab(self.csv_edit, "")
        self.gridLayout.addWidget(self.bgg_tabs, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 679, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.bgg_tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.searchLine, self.searchButton)
        MainWindow.setTabOrder(self.searchButton, self.gameCheck)
        MainWindow.setTabOrder(self.gameCheck, self.expanCheck)
        MainWindow.setTabOrder(self.expanCheck, self.bgg_tabs)
        MainWindow.setTabOrder(self.bgg_tabs, self.searchResults)
        MainWindow.setTabOrder(self.searchResults, self.addButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Board Game Name"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.expanCheck.setText(_translate("MainWindow", "Expansion"))
        self.gameCheck.setText(_translate("MainWindow", "Game"))
        self.csvImport.setText(_translate("MainWindow", "Import .csv"))
        self.searchResults.setSortingEnabled(True)
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.label_2.setText(_translate("MainWindow", "Selected Games"))
        self.dataCollectionStart.setText(_translate("MainWindow", "Start Data Collection"))
        self.bgg_tabs.setTabText(self.bgg_tabs.indexOf(self.bgg_search_tab), _translate("MainWindow", "BGG Search"))
        self.bgg_tabs.setTabToolTip(self.bgg_tabs.indexOf(self.bgg_search_tab), _translate("MainWindow", "Search Board Game Geek"))
        self.removeRow.setText(_translate("MainWindow", "Remove"))
        self.exportButton.setText(_translate("MainWindow", "Export"))
        self.bgg_tabs.setTabText(self.bgg_tabs.indexOf(self.csvPreview), _translate("MainWindow", "CSV Preview"))
        self.bgg_tabs.setTabText(self.bgg_tabs.indexOf(self.csv_edit), _translate("MainWindow", "CSV Edit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
