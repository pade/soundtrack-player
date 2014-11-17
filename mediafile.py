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

import os
import player

class MediaFile(object):
    '''
    Sound file class
    '''


    def __init__(self, filename):
        '''
        Create a MediaFile object
        @param filename: the full path of a sound track
        '''
        self._name = os.path.basename(filename)
        self._path = os.path.abspath(os.path.dirname(filename))
        self._type = ""
        self._media = player.Media(filename)
        
    def getFullName(self):
        ''' Return the full name (with absolute path) of the file '''
        
        fullname = self._path + os.pathsep + self._name
        return fullname
    
    def getName(self):
        ''' Return the filename (without path) '''
        
        return self._name
    
    def setName(self, name):
        ''' To change the displayed name of the media '''
        
        self._name = name
        
    def getDuration(self):
        ''' return the duration of the track
        @return: an integer that represents the track duration in second '''
        
        return self._media.getDuration()
    
