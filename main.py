# To run application/window

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from app import Ui_MainWindow
from api_functions import query
import sys
data = []
data.append(('Catan','1995','13','No'))
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchResults.setRowCount(1)
        self.ui.searchResults.setColumnCount(4)
        self.ui.searchResults.setHorizontalHeaderLabels(('Name','Year','UID','Expan?'))
        """row = 0
        for tup in data:
            col = 0
            for item in tup:
                gameinfo = QTableWidgetItem(item)
                self.ui.searchResults.setItem(row,col,gameinfo)
                col+=1
            row+=1"""

        self.ui.searchButton.clicked.connect(self.appendData(query("catan", self.ui.gameCheck.isChecked(), self.ui.expanCheck.isChecked())))

    def appendData(self,info):
        for i in range(len(info)):
            data.append(info[i])
        self.refreshData()

    def refreshData(self):
        self.ui.searchResults.setRowCount(len(data[0]))
        row = 0
        for tup in data:
            col = 0
            for item in tup:
                gameinfo = QTableWidgetItem(item)
                self.ui.searchResults.setItem(row,col,gameinfo)
                col += 1
            row += 1


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
