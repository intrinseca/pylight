'''
Created on 2 Dec 2012

@author: Michael
'''

from interface.cli import CLI
import unittest
from dmx.universe import Universe

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.uni = Universe()
        self.interface = CLI(self.uni)
        
    def tearDown(self):
        self.interface = None
        self.uni = None
        
    def testSingleChannel(self):
        self.interface.parseLine("1@128")
        self.assertEqual(self.uni.channels[0], 128)
        
        for i in range(1,256):
            self.assertEqual(self.uni.channels[i], 0, "Channel %s set incorrectly" % (i + 1))

    def testMultipleChannels(self):
        self.interface.parseLine("1-10@176")
        for i in range(0,10):
            self.assertEqual(self.uni.channels[i], 176, "Channel %s not set correctly" % (i + 1))
        
        for i in range(10, 256):
            self.assertEqual(self.uni.channels[i], 0, "Channel %s set incorrectly" % (i + 1))
    