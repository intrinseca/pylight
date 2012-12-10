from dmx import Universe

class Rig:
    heads = {}
    outputs = []
    
    def __init__(self):
        self.outputs = [Universe()]
    
    def refresh(self):
        for head_number, head in self.heads.iteritems():
            uni = self.outputs[head.address.universe - 1]
            i = 0
            
            for chan in head.getDMX():
                uni.channels[head.address.channel + i - 1] = chan
                i += 1