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

class Media(object):
    ''' Represent a media '''
    
    def __init__(self, filename):
        ''' Create a media object
        @param filename: full path of the file
        '''
        
        self._filename = filename
        
        # Initialize a VLC Instance
        self._vlc = vlc.Instance()
        try:
            self._media = self._vlc.media_new(self._filename)
            self._media.parse()
        except:
            raise
        
    def getDuration(self):
        ''' Return the duration of the track  
        @return: Duration of the track (round integer in second)'''
        return round(self._media.get_duration()/1000.0)
        