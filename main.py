# To run application/window

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QLabel
from PyQt5.QtGui import QPixmap
from app import Ui_MainWindow
from api_functions import query
import sys
import urllib
data = []


class mywindow(QtWidgets.QMainWindow):
    gamesToBeAdded = []
    ids_toAdd = []
    def __init__(self):
        super(mywindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchResults.setRowCount(0)
        self.ui.searchResults.setColumnCount(4)
        self.ui.searchResults.setHorizontalHeaderLabels(('Name','Year','UID','Type'))
        header = self.ui.searchResults.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.ui.searchButton.clicked.connect(self.api_search)
        self.ui.searchLine.returnPressed.connect(self.api_search)
        self.ui.addButton.clicked.connect(self.addIDs)
        self.ui.removeButton.clicked.connect(self.removeIDs)

    def api_search(self):
        answers = query(self.ui.searchLine.text(), self.ui.gameCheck.isChecked(), self.ui.expanCheck.isChecked())
        self.appendData(answers)

    def appendData(self,info):
        for i in range(len(info[0])):
            data.append((info[0][i],info[1][i],info[2][i],info[3][i]))
        self.refreshData()

    def refreshData(self):
        self.ui.searchResults.setRowCount(len(data))
        row = 0
        for tup in data:
            col = 0
            for item in tup:
                gameinfo = QTableWidgetItem(item)
                self.ui.searchResults.setItem(row,col,gameinfo)
                col += 1
            row += 1
        header = self.ui.searchResults.horizontalHeader()
        #header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        data.clear()

    def addIDs(self):
        addedGames = []
        for idx in self.ui.searchResults.selectionModel().selectedRows():
            if(self.ui.searchResults.item(idx.row(),2).text() not in self.ids_toAdd):
                self.ids_toAdd.append(self.ui.searchResults.item(idx.row(),2).text())
                name = self.ui.searchResults.item(idx.row(),0).text()
                year = self.ui.searchResults.item(idx.row(),1).text()
                self.gamesToBeAdded.append("%s (%s)" % (name, year))
                addedGames.append("%s (%s)" % (name, year))
            else:
                print("%s already in list" % (self.ui.searchResults.item(idx.row(),0).text()))

        #print("")
        #print(self.ui.selectedGamees.count())
        #self.ui.selectedGamees.setRowCount(len(gamesToBeAdded))
        row = 0
        for game in addedGames:
            #info = QListWidgetItem(game)
            self.ui.selectedGamees.insertItem(self.ui.selectedGamees.count(),game)
            #row += 1
        addedGames.clear()

    def removeIDs(self):
        #listedgames = gamesToBeAdded

        for j in range(len(self.ids_toAdd)):
            print(self.gamesToBeAdded[j], self.ids_toAdd[j])


        r_idxs = []
        for idx in self.ui.selectedGamees.selectionModel().selectedRows():
            gamename = self.ui.selectedGamees.item(idx.row()).text()
            r_idxs.append(self.gamesToBeAdded.index(gamename))
            self.gamesToBeAdded = [x for x in self.gamesToBeAdded if x is not gamename]

        for item in self.ui.selectedGamees.selectedItems():
            self.ui.selectedGamees.takeItem(self.ui.selectedGamees.row(item))

        for i in r_idxs:
            del self.ids_toAdd[i]

        print("")
        for j in range(len(self.ids_toAdd)):
            print(self.gamesToBeAdded[j], self.ids_toAdd[j])

    def refreshList(self):
        pass


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
