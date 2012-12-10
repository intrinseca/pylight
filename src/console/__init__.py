from dmx import Universe
from console.animation import State

class Rig:    
    def __init__(self):
        self.heads = {}
        self.outputs = [Universe()]
    
    def refresh(self):
        for headNumber, head in self.heads.iteritems():
            uni = self.outputs[head.address.universe - 1]
            i = 0
            
            for chan in head.getDMX():
                uni.channels[head.address.channel + i - 1] = chan
                i += 1

class Show:
    def __init__(self, rig):
        self.rig = rig
        self.theatre_mode = True #Theatre Mode: Record all heads for each state
        self.programming_mode = False #Programming Mode: Don't update the outputs
        self.states = []
    
    def recordNewState(self):
        s = State()
        s.save(self.rig.heads)
        self.states.append(object)
    
    def loadSavedState(self, state):
        state.restore(self.rig.heads)
    
    def refresh(self):
        if not self.programming_mode:
            self.rig.refresh()
    