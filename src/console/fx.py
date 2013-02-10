class FXBase:
    def __init__(self):
        self.spread = 1
        self.size = 1
        self.channels = []
    
    def apply(self, head_index, head, step):
        pass

class StaticIntensity(FXBase):
    def __init__(self):
        FXBase.__init__(self)
        self.channels = ["MasterIntensity"]
    
    def apply(self, head_index, head, step):
        head.attributes["MasterIntensity"].value = int(self.size * 255)