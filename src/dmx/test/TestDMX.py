import unittest

from dmx.universe import Universe

class TestDMX(unittest.TestCase):
    
    def setUp(self):
        self.uni = Universe()
        
    def tearDown(self):
        self.uni = None
        
    def testRead(self):
        for i in range(0,256):
            self.assertEqual(self.uni.channels[i], 0, "Channel %d not initialised" % i)
            
    def testSet(self):
        for i in range(0, 256):
            self.uni.channels[i] = i
            
        for i in range(0,255):
            self.assertEqual(self.uni.channels[i], i, "Channel %d value not recorded" % i)
