'''
Created on 27 août 2014

@author: dassier
'''


from PyQt5 import QtMultimedia
from PyQt5.QtCore import QUrl


def main():

    player = QtMultimedia.QMediaPlayer()
    file = QUrl.fromLocalFile("/home/dassier/workspace/qtaudio/accident.mp3")
    media = QtMultimedia.QMediaContent(file)
    player.setMedia(media)

    
    

if __name__ == '__main__':
    main()