'''
Created on 2 Dec 2012

@author: Michael
'''

import unittest

from console import Rig
from console.heads import Dimmer
from interface.parsers import CLI

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.rig = Rig()

        for i in range(1, 25):
            d = Dimmer(1, i)
            self.rig.heads[i] = d
            d.intensity.value = 0
        
        self.parser = CLI(self.rig)
        
    def tearDown(self):
        self.interface = None
        self.uni = None
        
    def testSingleChannel(self):
        self.parser.parseLine("1@128")
        
        self.assertEqual(self.rig.outputs[0].channels[0], 128)
        
        for i in range(1,256):
            self.assertEqual(self.rig.outputs[0].channels[i], 0, "Channel %s set incorrectly" % (i + 1))

    def testMultipleChannels(self):
        self.parser.parseLine("1-10@176")
        for i in range(0,10):
            self.assertEqual(self.rig.outputs[0].channels[i], 176, "Channel %s not set correctly" % (i + 1))
        
        for i in range(10, 256):
            self.assertEqual(self.rig.outputs[0].channels[i], 0, "Channel %s set incorrectly" % (i + 1))
    