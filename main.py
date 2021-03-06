# To run application/window

from PyQt5 import QtWidgets
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QTableWidgetItem, QLabel, QTabWidget, QFileDialog, QTableView, QWidget, QDialog
#from PyQt5.QtGui import QPixmap
from app import Ui_MainWindow
from info import Ui_MainWindow as window2
from aboutD import Ui_Dialog as about
from api_functions import query, grabInfo
import sys
import pandas as pd
import csv
from datetime import datetime

#import urllib
data = []
info = {}
#csv_preview = pd.DataFrame()

class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent = None):
        return self._data.shape[0]

    def columnCount(self, parent = None):
        return self._data.shape[1]

    def data(self, index, role = Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class aboutPopup(QDialog):
    def __init__(self, parent = None):
        super(aboutPopup,self).__init__(parent)
        self.ui = about()
        self.ui.setupUi(self)

class infoWindow(QtWidgets.QMainWindow):
    csv_preview = pd.DataFrame()

    def __init__(self,parent=None):
        super(infoWindow,self).__init__(parent)
        self.ui = window2()
        self.ui.setupUi(self)

        self.ui.cancelButton.clicked.connect(self.close)
        self.ui.grabButton.clicked.connect(self.passInfo)
        #self.ui.grabButton.clicked.connect(self.parent().previewBExp)
        #self.parent().previewBExp

    def close(self):
        self.hide()

    def passInfo(self):
        info.clear()
        info.update([('id',self.ui.bggUID.isChecked()), ('age',self.ui.age.isChecked()), ('players',self.ui.nPlayers.isChecked()), ('name',self.ui.name.isChecked()), ('playtime',self.ui.playTime.isChecked()), ('year',self.ui.year.isChecked()), ('artists',self.ui.artists.isChecked()), ('categories',self.ui.categories.isChecked()), ('designers',self.ui.designers.isChecked()), ('expans',self.ui.expans.isChecked()), ('mechanisms',self.ui.mechanisms.isChecked()), ('expans_c',self.ui.nExpan.isChecked()), ('publisher',self.ui.publisher.isChecked()), ('bbg_rank',self.ui.bgg_rank.isChecked()), ('bestPlayers',self.ui.bnPlayers.isChecked()), ('complexity',self.ui.complexity.isChecked()), ('ratings_c',self.ui.nRatings.isChecked()), ('rating',self.ui.rating.isChecked()), ('image',self.ui.image.isChecked()), ('description',self.ui.description.isChecked()), ('link',self.ui.bgg_link.isChecked())])
        #print(info)
        #self.csv_preview = pd.DataFrame()

        self.csv_preview = self.csv_preview.append(grabInfo(info, Window.ids_toAdd))
        #print(self.csv_preview)
        self.parent().ui.bgg_tabs.setTabEnabled(1,True)
        self.parent().ui.bgg_tabs.setCurrentIndex(1)
        self.parent().ui.dfPreview.setEnabled(True)

        #self.setPreview()
        #self.parent().dfExport = self.csv_preview
        self.parent().dfExport = self.parent().dfExport.append(self.csv_preview)
        self.setPreview()
        #Window.dfExport = self.csv_preview
        self.parent().clearGTA()
        self.parent().ui.selectedGamees.clear()
        self.close()

    def setPreview(self):
        #model = pandasModel(self.csv_preview)
        model = pandasModel(self.parent().dfExport)
        self.parent().ui.dfPreview.setModel(model)

class Window(QtWidgets.QMainWindow):

    # Variables used across multiple functions
    gamesToBeAdded = []
    ids_toAdd = []
    dfExport = pd.DataFrame()


    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.about = aboutPopup(parent=self)
        self.popUp = infoWindow(parent=self)
        self.ui.searchResults.setRowCount(0)
        self.ui.searchResults.setColumnCount(4)
        self.ui.searchResults.setHorizontalHeaderLabels(('Name','Year','UID','Type'))
        header = self.ui.searchResults.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #self.popUp = infoWindow()

        self.ui.bgg_tabs.setTabEnabled(1, False)
        #self.ui.bgg_tabs.setCurrentIndex(0)
        self.ui.bgg_tabs.setTabEnabled(2, False)
        #self.ui.dfPreview.setEnabled(True)

        self.ui.searchButton.clicked.connect(self.api_search)
        self.ui.searchButton.clicked.connect(self.searchIndex)
        self.ui.searchLine.returnPressed.connect(self.api_search)
        self.ui.searchLine.returnPressed.connect(self.searchIndex)
        self.ui.addButton.clicked.connect(self.addIDs)
        self.ui.addButton.clicked.connect(self.enableButton)
        self.ui.removeButton.clicked.connect(self.removeIDs)
        self.ui.dataCollectionStart.clicked.connect(self.newWindow)
        #self.ui.exportButton.clicked.connect(self.updateExport)
        self.ui.exportButton.clicked.connect(self.saveFileDialog)
        self.ui.searchResults.itemDoubleClicked.connect(self.addIDs)
        self.ui.searchResults.itemDoubleClicked.connect(self.enableButton)
        self.ui.selectedGamees.itemDoubleClicked.connect(self.removeIDs)
        #self.ui.dfPreview.itemDoubleClicked.connect(self.dfRemoveRow)
        self.ui.removeRow.clicked.connect(self.dfRemoveRow)
        self.ui.actionAbout.triggered.connect(self.showAbout)
        self.ui.csvImport.clicked.connect(self.openFileNameDialog)
        self.ui.actionOpen.triggered.connect(self.openFileNameDialog)

    def clearGTA(self):
        self.gamesToBeAdded.clear()

    def searchIndex(self):
        self.ui.bgg_tabs.setCurrentIndex(0)

    def showAbout(self):
        self.about.show()

    def dfRemoveRow(self):
        for idx in self.ui.dfPreview.selectionModel().selectedRows():
            #print(idx.row())
            row = int(idx.row())
            #print(self.dfExport.iloc[row])
            self.dfExport.drop(self.dfExport.index[row], inplace = True)
        self.updatePreview()

    def updatePreview(self):
        model = pandasModel(self.dfExport)
        self.ui.dfPreview.setModel(model)

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
        r_idxs = []
        for idx in self.ui.selectedGamees.selectionModel().selectedRows():
            gamename = self.ui.selectedGamees.item(idx.row()).text()
            r_idxs.append(self.gamesToBeAdded.index(gamename))
            self.gamesToBeAdded.remove(gamename)
        for item in self.ui.selectedGamees.selectedItems():
            self.ui.selectedGamees.takeItem(self.ui.selectedGamees.row(item))
        for i in r_idxs:
            del self.ids_toAdd[i]

    def newWindow(self):
        #self.w = infoWindow()
        self.popUp.show()

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        #now = datetime.now()
        #dt1 = now.strftime("%H:%M_%D-%M-%y")
        #defaultName = dt1 + "_exp"
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","",".csv Files (*.csv)", options=options)
        print(fileName)
        if fileName:
            #print(fileName)
            #print(self.dfExport)
            #print(type(fileName))
            if(fileName.endswith('.csv')):
                expName = fileName
                print(fileName)
                print(expName)
            else:
                expName = fileName + ".csv"
            self.dfExport.to_csv(expName, encoding = 'utf-8-sig', quoting=csv.QUOTE_MINIMAL, index = False)
        else:
            print('nothing')

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        #fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",".csv Files (*.csv)", options = options)
        #if fileName:
        #    print(fileName)
        fileURL, _ = QFileDialog.getOpenFileUrl(self,"QFileDialog.getOpenFileUrl()", "",".csv Files (*.csv)", options = options)
        print(fileURL)
        if (fileURL.toString() != ''):
            self.dfExport = pd.read_csv(fileURL.toString(), index_col = False)
            self.ui.bgg_tabs.setTabEnabled(1,True)
            self.ui.bgg_tabs.setCurrentIndex(1)
            self.ui.dfPreview.setEnabled(True)
            self.updatePreview()
        else:
            print('nada')


app = QtWidgets.QApplication([])
application = Window()
application.show()
sys.exit(app.exec())
