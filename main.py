# To run application/window

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QLabel
from PyQt5.QtGui import QPixmap
from app import Ui_MainWindow
from api_functions import query
import sys
import urllib
data = []
#data.append(('Catan','1995','13','No'))
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchResults.setRowCount(1)
        self.ui.searchResults.setColumnCount(4)
        self.ui.searchResults.setHorizontalHeaderLabels(('Name','Year','UID','Type'))
        header = self.ui.searchResults.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.ui.searchButton.clicked.connect(self.api_search)
        self.ui.searchLine.returnPressed.connect(self.api_search)

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
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        data.clear()




app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
