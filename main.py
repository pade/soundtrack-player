'''
Created on 27 août 2014

@author: dassier
'''


from mediafile import MediaFile
import vlc
import os

def main():
    
    fichier = "./test/example.mp3"

    m = MediaFile(fichier)

    vlcInstance = vlc.Instance()
    player = vlcInstance.media_player_new()
    player.set_media(m.getMedia())
    player.play()
    
    input("Press a key")
    
    

if __name__ == '__main__':
    main()