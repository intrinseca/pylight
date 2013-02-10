from dmx import Universe
from console.animation import State

class Rig:    
    def __init__(self):
        self.heads = {}
        self.outputs = [Universe()]
    
    def reset(self):
        for head in self.heads.itervalues():
            head.reset()
    
    def refresh(self):
        for head in self.heads.itervalues():
            uni = self.outputs[head.address.universe - 1]
            i = 0
            
            for chan in head.getDMX():
                uni.channels[head.address.channel + i - 1] = chan
                i += 1

class Show:
    def __init__(self, rig):
        self.rig = rig
        self.states = []
        self.sequences = []
        self.programmer = State()
        
        self.programming_mode = False #Programming Mode: Don't update the outputs
    
    def saveState(self):
        self.states.append(self.programmer)
        self.clearProgrammer()
    
    def restoreState(self, state):
        self.programmer = state
    
    def clearProgrammer(self):        
        self.programmer = State()
        self.rig.reset()
    
    def refresh(self):
        if not self.programming_mode:
            self.programmer.apply(self.rig.heads)
            self.rig.refresh()
    