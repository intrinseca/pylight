from dmx import Universe

class Rig:
    heads = []
    outputs = []
    
    def __init__(self):
        self.outputs = [Universe()]
    
    def refresh(self):
        for head in self.heads:
            uni = self.outputs[head.address.universe - 1]
            i = 0
            
            for chan in head.getDMX():
                uni.channels[head.address.channel + i - 1] = chan
                i += 1