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

class MediaFileError(Exception):
    
    def __init__(self, message="MediaFileError"):
        # Call the base class constructor with the parameters it needs
        super(MediaFileError, self).__init__(message)   
        self.message = message
        
    def __str__(self):
        return self.message

class MediaFileNotFound(MediaFileError):
    
    def __init__(self, filename):
        self.message = "File not found: {}".format(filename)
        super(MediaFileNotFound, self).__init__(self.message)


class MediaFile(object):
    '''
    Sound file class
    '''

    def __init__(self, filename):
        '''
        Create a MediaFile object
        @param filename: the full path of a sound track
        '''
        
        if  not os.path.isfile(filename):
            raise MediaFileNotFound(filename)

        self._name = os.path.basename(filename)
        self._path = os.path.abspath(os.path.dirname(filename))
        self._type = ""
#         self._media = player.Player(filename)        
        
    def getFullName(self):
        ''' Return the full name (with absolute path) of the file '''
        
        fullname = os.path.join(self._path, self._name)
        return fullname
    
    def getName(self):
        ''' Return the filename (without path) '''
        
        return self._name
    
    def setName(self, name):
        ''' To change the displayed name of the media '''
        self._name = name
        
#     def getDuration(self):
#         ''' return the duration of the track
#         @return: an integer that represents the track duration in second '''
#         
#         return self._media.getDuration()
    
#     def getMedia(self):
#         return self._media.getMedia()
