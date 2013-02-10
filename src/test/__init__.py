from console import Rig
from console.heads import Dimmer

def createSampleRig():
    r = Rig()

    for i in range(1, 25):
        d = Dimmer(1, i)
        r.heads[i] = d
        d.attributes["MasterIntensity"].value = 0
    
    r.refresh()
    
    return r