'''
Created on 2 Dec 2012

@author: Michael
'''

import unittest

from console import Show
from interface.parsers import CLI
from test import createSampleRig

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.rig = createSampleRig()
        self.show = Show(self.rig)
        
        self.parser = CLI(self.show)
        
    def tearDown(self):
        self.interface = None
        self.uni = None
        
    def testSingleChannel(self):
        self.parser.parseLine("1@128")
        self.show.refresh()
        
        self.assertEqual(self.rig.outputs[0].channels[0], 128)
        
        for i in range(1,256):
            self.assertEqual(self.rig.outputs[0].channels[i], 0, "Channel %s set incorrectly" % (i + 1))

    def testMultipleChannels(self):
        self.parser.parseLine("1-10@176")        
        self.show.refresh()
        
        for i in range(0,10):
            self.assertEqual(self.rig.outputs[0].channels[i], 176, "Channel %s not set correctly" % (i + 1))
        
        for i in range(10, 256):
            self.assertEqual(self.rig.outputs[0].channels[i], 0, "Channel %s set incorrectly" % (i + 1))
    
    def testState(self):
        for i in range(1, 25):
            self.parser.parseLine("{0}@{1:00}".format(i, i * 10))
        
        self.parser.parseLine("save")
        self.parser.parseLine("1-24@00")
        self.show.refresh()
        self.parser.parseLine("restore 1")
        self.show.refresh()
        
        for i in range(1, 25):
            self.assertEqual(self.rig.outputs[0].channels[i - 1], i * 10, "Channel %s not restored" % (i + 1))
    