import unittest
from test import createSampleRig
from console.animation import State

class TestAnimation(unittest.TestCase):
    def setUp(self):
        self.rig = createSampleRig()

    def tearDown(self):
        self.rig = None

    def testSavedState(self):
        for i in range(1,11):
            self.rig.heads[i].attributes["MasterIntensity"].value = i * 10
        
        s = State()
        s.save(self.rig.heads)
        
        for i in range(1,11):
            self.rig.heads[i].attributes["MasterIntensity"].value = 0
        
        s.restore(self.rig.heads)
        
        for i in range(1,11):
            self.assertEqual(self.rig.heads[i].attributes["MasterIntensity"].value, i * 10, "State not restored")