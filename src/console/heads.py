from console.attributes import IntensityAttribute, RGBColorAttribute
from dmx import Address

class Head:    
    def __init__(self, universe, startChannel, channels):
        self.address = Address(universe, startChannel)
        self.channels = channels
        assert(self.address.channel + (self.channels - 1) <= 256)
        
        self.attributes = {}
        self.attributes["MasterIntensity"] = IntensityAttribute()
    
    def intensity(self):
        return self.attributes["MasterIntensity"].value
    
    def getDMX(self):
        return [self.intensity()]
    
class Dimmer(Head):
    def __init__(self, universe, startChannel):
        Head.__init__(self, universe, startChannel, 1)
    
    def __str__(self):
        return "I: %2d" % self.intensity.value

class FourChannelLED(Head):
    def __init__(self, universe, startChannel):
        Head.__init__(self, universe, startChannel, 4)
        self.attributes["Color"] = RGBColorAttribute(0, 0, 0)
    
    def getDMX(self):
        return [self.intensity(), self.color.r, self.color.g, self.color.b]

class ThreeChannelLED(Head):
    def __init__(self, universe, startChannel):
        Head.__init__(self, universe, startChannel, 3)
        self.attributes["Color"] = RGBColorAttribute(0, 0, 0)
    
    def getDMX(self):
        return [int(x * self.intensity()) for x in [self.color.r, self.color.g, self.color.b]]