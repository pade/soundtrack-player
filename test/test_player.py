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
import sys
import unittest

# try import: necessary because in case of starting only this test, path is not set at this point
try:
    import player
except:
    pass


class TestPlayer(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_duration(self):
        ''' Create a new media and get its duration'''
        m = player.Media("example.mp3")
        duration = m.getDuration()
        self.assertEqual(duration, 170)
        
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPlayer))
    return suite

if __name__ == "__main__":
    
    # Set parent directory in path, to be able to import module
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    import player
    
    suite = suite()
    unittest.TextTestRunner(verbosity=2).run(suite)  