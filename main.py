# Sep, 19, 2023
# Mersad23Akbari@gmail.com

import requests
import json 
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
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Dota2 tracker by m23rsad'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()
    
    def initUI(self):
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
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
	
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        account_id = textboxValue
        URL = f"https://api.opendota.com/api/players/{account_id}/peers"
        r = requests.get(url = URL)
        data = r.json()
        names = ""
        for name in data:
               names = names + str(name['personaname'])+"\n"
        QMessageBox.question(self, 'Here U are', "your peers are " + names , QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
	
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
