class FXBase:
    def __init__(self):
        self.spread = 1
        self.size = 1
        self.time = 2
    
    def apply(self, head_index, head_count, head, step):
        pass

class StaticIntensity(FXBase):    
    def apply(self, head_index, head_count, head, step):
        head.attributes["MasterIntensity"].value = int(self.size * 255)

class IntensityRamp(FXBase):
    def apply(self, head_index, head_count, head, step):
        step = (step + ((float(head_index) / head_count))) % 1
        head.attributes["MasterIntensity"].value = int(self.size * step * 255)