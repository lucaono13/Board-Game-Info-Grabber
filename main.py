# To run application/window

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QLabel, QTabWidget
#from PyQt5.QtGui import QPixmap
from app import Ui_MainWindow
from info import Ui_MainWindow as window2
from api_functions import query, grabInfo
import sys
import pandas as pd

#import urllib
data = []
info = {}

class infoWindow(QtWidgets.QMainWindow):
    csv_preview = pd.DataFrame()

    def __init__(self):
        super(infoWindow,self).__init__()
        self.ui = window2()
        self.ui.setupUi(self)

        self.ui.cancelButton.clicked.connect(self.close)
        self.ui.grabButton.clicked.connect(self.passInfo)
        #self.ui.grabButton.clicked.connect(Window.previewBExp)

    def close(self):
        self.hide()

    def passInfo(self):
        info.clear()
        info.update([('id',self.ui.bggUID.isChecked()), ('age',self.ui.age.isChecked()), ('players',self.ui.nPlayers.isChecked()), ('name',self.ui.name.isChecked()), ('playtime',self.ui.playTime.isChecked()), ('year',self.ui.year.isChecked()), ('artists',self.ui.artists.isChecked()), ('categories',self.ui.categories.isChecked()), ('designers',self.ui.designers.isChecked()), ('expans',self.ui.expans.isChecked()), ('mechanisms',self.ui.mechanisms.isChecked()), ('expans_c',self.ui.nExpan.isChecked()), ('publisher',self.ui.publisher.isChecked()), ('bbg_rank',self.ui.bgg_rank.isChecked()), ('bestPlayers',self.ui.bnPlayers.isChecked()), ('complexity',self.ui.complexity.isChecked()), ('ratings_c',self.ui.nRatings.isChecked()), ('rating',self.ui.rating.isChecked()), ('image',self.ui.image.isChecked()), ('description',self.ui.description.isChecked()), ('link',self.ui.bgg_link.isChecked())])
        #print(info)
        #csv_preview = pd.DataFrame()

        self.csv_preview = self.csv_preview.append(grabInfo(info, Window.ids_toAdd))
        self.hide()
        Window.previewBExp


class Window(QtWidgets.QMainWindow):

    # Variables used across multiple functions
    gamesToBeAdded = []
    ids_toAdd = []


    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchResults.setRowCount(0)
        self.ui.searchResults.setColumnCount(4)
        self.ui.searchResults.setHorizontalHeaderLabels(('Name','Year','UID','Type'))
        header = self.ui.searchResults.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.ui.bgg_tabs.setTabEnabled(1, False)
        self.ui.bgg_tabs.setTabEnabled(2, False)

        self.ui.searchButton.clicked.connect(self.api_search)
        self.ui.searchLine.returnPressed.connect(self.api_search)
        self.ui.addButton.clicked.connect(self.addIDs)
        self.ui.addButton.clicked.connect(self.enableButton)
        self.ui.removeButton.clicked.connect(self.removeIDs)
        self.ui.dataCollectionStart.clicked.connect(self.newWindow)

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
        for game in addedGames:
            self.ui.selectedGamees.insertItem(self.ui.selectedGamees.count(),game)
        addedGames.clear()
        self.ui.searchResults.selectionModel().clearSelection()

    def enableButton(self):
        self.ui.dataCollectionStart.setEnabled(True)

    def removeIDs(self):
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

    def newWindow(self):
        self.w = infoWindow()
        self.w.show()

    def previewBExp(self):
        #self.ui.bgg_tabs.setTabEnabled(1)
        self.ui.bgg_tabs.setCurrentIndex(1)

app = QtWidgets.QApplication([])
application = Window()
application.show()
sys.exit(app.exec())
