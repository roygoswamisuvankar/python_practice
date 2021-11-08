from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QScrollArea, QFrame, QPushButton, QFileDialog, QListWidget
from PyQt5 import uic
import sys
import re
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("dataFind.ui",self)
        Title = 'Email Finder'
        self.setWindowTitle(Title)

        #define widgets
        self.label = self.findChild(QLabel,"label")
        self.label2 = self.findChild(QLabel,"label2")
        self.button = self.findChild(QPushButton,"pushButton")
        self.list = self.findChild(QListWidget, "listWidget")
        #self.find1 = self.findChild(QPushButton, "Find")
        #connection
        self.button.clicked.connect(self.MyFunction)
        #self.find1.clicked.connect(self.FindEmails1)
        self.show()


    def MyFunction(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '','All Files (*.*)')
        if path != ('', ''):
            print("File path : " + path[0])
            self.label2.setText(path[0])
            self.FindEmails(path[0])

    def FindEmails(self, f):
        fileOpen = open(f,"r")
        j = 0
        a = 0
        for i in fileOpen:
            lst = re.findall('\S+@\S+',i)
            for k in lst:
                self.list.insertItem(j - 1, f'{a, k}')
                a = a + 1

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
