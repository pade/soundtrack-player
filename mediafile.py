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

class MediaFile(object):
    '''
    Sound file class
    '''


    def __init__(self, filename = ""):
        '''
        Constructor
        '''
        self.name = os.path.basename(filename)
        self.path = os.path.abspath(os.path.dirname(filename))
        self.type = ""
        self.duration = 0
        
    def getFullName(self):
        ''' Return the full name (with absolute path) of the file '''
        
        fullname = None
        if self.name != "":
            fullname = self.path + os.pathsep + self.name
        return fullname
    
