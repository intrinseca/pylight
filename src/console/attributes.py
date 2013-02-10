class IntensityAttribute:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.value = 0        
    
    def percentage(self):
        return self.value / 255.0;
    
    def __str__(self):
        return "{:000}".format(self.value)

class PositionAttribute:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.pan = 0
        self.tilt = 0

class RGBColorAttribute:
    def __init__(self):  
        self.reset()
    
    def reset(self, r = 0, g = 0, b = 0):
        self.r = r
        self.g = g
        self.b = b