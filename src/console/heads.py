from console.attributes import IntensityAttribute, RGBColorAttribute
from dmx import Address

class Head:    
    def __init__(self, universe, startChannel, channels):
        self.address = Address(universe, startChannel)
        self.intensity = IntensityAttribute()
        self.channels = channels
        assert(self.address.channel + (self.channels - 1) <= 256)
    
    def getDMX(self):
        return [self.intensity.value]
    
class Dimmer(Head):
    def __init__(self, universe, startChannel):
        Head.__init__(self, universe, startChannel, 1)
    
    def __str__(self):
        return "I: %2d" % self.intensity.value

class FourChannelLED(Head):
    def __init__(self, universe, startChannel):
        Head.__init__(self, universe, startChannel, 4)
        self.color = RGBColorAttribute(0, 0, 0)
    
    def getDMX(self):
        return [self.intensity.value, self.color.r, self.color.g, self.color.b]
    