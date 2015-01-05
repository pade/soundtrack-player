'''
Created on 27 août 2014

@author: dassier
'''


from mediafile import MediaFile
import vlc
import os
import sys
import main_ui

import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow


class Gui(QMainWindow):
	
	def __init__(self):
		super().__init__()
		self.ui = main_ui.Ui_MainWindow()
		self.ui.setupUi(self)
		

def test_main():
    
    fichier = "./test/example.mp3"

    m = MediaFile(fichier)

    vlcInstance = vlc.Instance()
    player = vlcInstance.media_player_new()
    player.set_media(m.getMedia())
    player.play()
    
    input("Press a key")
    
def  main(args=[]):
	app = QApplication(args)
	
	myui = Gui()
	myui.show()
	
	
	sys.exit(app.exec_())

if __name__ == '__main__':
	main(sys.argv)
    

	
	
