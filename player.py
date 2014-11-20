'''
This file is part of the software.

    This software is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This software is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
'''


import vlc
import os.path
from vlc import track_description_list

class PlayerError(Exception):
    
    def __init__(self, message="PlayerError"):
        # Call the base class constructor with the parameters it needs
        super(PlayerError, self).__init__(message)
        
        self.message = message
        
    def __str__(self):
        return self.message


class Player(object):
    ''' Represent a media '''
    
    _vlc_instance = None

    def _getMedia(self):
        return self._media
    
    def _createPlayer(self, media):
        ''' Create a new player
        @param media: a Media object to be read by the player
        @return: a tuple composed by a Player object, and a EventManager object
        '''
        new_player = self._vlc.media_player_new()
        new_player.set_media(media)
        new_player_events = new_player.event_manager()
        new_player_events.event_attach(vlc.EventType.MediaPlayerEndReached, self._trackFinished)
        return new_player, new_player_events
    
    def _trackFinished(self, event):
        ''' Callback function call when the track is finished'''
        if self.isrepeat():
            # to repeat the track, create a new player
            self._player, self._player_event = self._createPlayer(self._getMedia())
            self.play()
        
    
    def __init__(self, mediafile):
        ''' Create a media object
        @param mediafile: a MediaFile object
        '''   
        self._mediafile = mediafile
                
        # Initialize a VLC Instance or retreive the instance already created
        if self.__class__._vlc_instance is None:
            self.__class__._vlc_instance = vlc.Instance()
            
        self._vlc = self.__class__._vlc_instance
        
        self._media = self._vlc.media_new(self._mediafile.getFullName())
        self._media.parse()
        
        self._player, self._player_event = self._createPlayer(self._getMedia())
        
        self._repeat = False
                
    def getDuration(self):
        ''' Return the duration of the track  
        @return: Duration of the track (round integer in second)'''
        return round(self._media.get_duration()/1000.0)
          
    def play(self):
        ''' Play the media file'''
        if not self._player.is_playing():
            self._player.play()
        
    def pause(self):
        '''Pause the current play'''
        self._player.pause()
    
    def stop(self):
        '''Stop the current play'''
        self._player.stop()
        
    def repeat(self, mode):
        '''Repeat mode
        @param mode: True to repeat the track, False to not repeat
        '''
        if mode is True:
            self._repeat = True
        else:
            self._repeat = False
            
    def isRepeat(self):
        return self._repeat
    
    def getPosition(self):
        ''' Get the actual position in the track
        @return: position in the track (0: begining, 1: end)
        '''
        return self._player.get_position()
    
    def setPosition(self, value):
        ''' Set the position of the track
        @param value: an integer between 0 and 1 (0: set at the begining, 1 at the end)
        '''
        if value >= 0 and value <= 1:
            self._player.set_position(value)
    
    def setVolume(self, volume):
        ''' Set the track volume
        @param volume: the volume, 0: mute, 1: the max
        '''
        if volume >= 0.0 and volume <= 1.0:
            self._player.audio_set_volume(volume*100)
            
    def getVolume(self):
        ''' Get volume of the current track
        @return: the volume, 0: mute, 1: the max
        '''
        return round(self._player.audio_get_volume()/100.0, 2)