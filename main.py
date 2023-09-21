# Sep, 19, 2023
# Mersad23Akbari@gmail.com

import requests
import urllib.request
import json
import os

#Check if pyqt is installd, install it if not
os.system("sudo pip install -r requirements.txt") 
'''
data = r.json()
players = data['players']
for player in players:
	try:
		print(player['personaname'])
	except:
		continue
f = open("demofile2.txt", "a")
f.write(str(data))
f.close()
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QMenuBar, QMenu, QRadioButton, QLabel

from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap,QFont
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore
app = QApplication(sys.argv)
def darkmode():
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette) 
def lightmode():
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(172, 179, 194))
    palette.setColor(QPalette.WindowText, Qt.black)
    palette.setColor(QPalette.Base, QColor(108, 119, 130))
    palette.setColor(QPalette.AlternateBase, QColor(172, 179, 194))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.black)
    palette.setColor(QPalette.Text, Qt.black)
    palette.setColor(QPalette.Button, QColor(172, 179, 194))
    palette.setColor(QPalette.ButtonText, Qt.black)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.white)
    app.setPalette(palette) 

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Dota2 tracker by m23rsad'
        self.left = 10
        self.top = 10
        self.width = 420
        self.height = 380
        self.initUI()
        self.statusBar().showMessage('GitHub.com/MersadAkbari')        
        lightmode()
       # adding 2 checkboxes for theme switch
        

    def initUI(self):
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        self.textbox.setPlaceholderText("Enter your account id here.") 
        # Create a button in the window
        self.button = QPushButton('Submit', self)
        self.button.move(20,80)
        self.setWindowIcon(QIcon("Cat.svg"))
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        # creating a push button
        self.button2 = QPushButton("Enter Dark Mode", self)
        # setting geometry of button
        self.button2.move(20,160) 
        # setting checkable to true
        self.button2.setCheckable(True)
        self.button2.setChecked(True)
        # setting calling method by button
        self.button2.clicked.connect(self.changeColor)
        # setting default color of button to light-grey
        self.button2.setStyleSheet("background-color : lightgrey")
 
        # show all the widgets
        self.update()
        self.show()
   
    # method called by button
    def changeColor(self):
 
        # if button is checked
        if self.button2.isChecked():
            lightmode()
            # setting background color to light-blue
            self.button2.setText("Enter Dark Mode")             
            app.setStyle("")
        # if it is unchecked
        else:
            
            # set background color back to light-grey
            darkmode()
            self.button2.setText("Enter Light Mode") 
	
    @pyqtSlot()
    def on_click(self):
        self.label3.setText(f"")
        self.label4.setText(f"")

        textboxValue = self.textbox.text()
        account_id = textboxValue
        URL = f"https://api.opendota.com/api/players/{account_id}/peers"
        r = requests.get(url = URL)
        data = r.json()
        names = ""
        for name in data:
               names = names + str(name['personaname'])+"\n"
        QMessageBox.question(self, 'Here U are', "your team mates are : " + names , QMessageBox.Ok, QMessageBox.Ok)
        self.label2 = QLabel(self)
        URL_account = f"https://api.opendota.com/api/players/{account_id}"
        ra = requests.get(url = URL_account)
        data_a = ra.json()
        personaname = data_a["profile"]["personaname"]
        avatar = data_a["profile"]["avatar"]
        data_avatar = urllib.request.urlretrieve(avatar)



        #win and loses
        URL_wl = f"https://api.opendota.com/api/players/{account_id}/wl"
        rwl = requests.get(url = URL_wl)
        data_a = rwl.json()
        win = data_a["win"]
        lose = data_a["lose"]
        #label for win and loses
        self.label4.setText(f"Wins: {win}, Lose: {lose}")
        self.label4.move(50,300) 
        self.label4.setStyleSheet("border: 1px solid green;")        # loading image
        self.label4.setFont(QFont('Arial', 15))
        self.label4.resize(320,50)
        



        self.label3.setText(f"Hi, {personaname}")
        self.label3.move(50,220) 
        self.label3.setStyleSheet("border: 1px solid black;")        # loading image
        self.label3.setFont(QFont('Arial', 15))
        self.label3.resize(320,50)
        
        self.pixmap = QPixmap(str(data_avatar))
 
        # adding image to label
        self.label2.setPixmap(self.pixmap)
 
        # Optional, resize label to image size

        self.label2.move(20,220) 
        self.label2.resize(self.pixmap.width(),
                self.pixmap.height())

        # show all the widgets
        self.label2.show()
        self.label3.show()
        self.label4.show()
        self.textbox.setText("")

if __name__ == '__main__':
    app.setStyle("Fusion")
    ex = App()
    sys.exit(app.exec_())