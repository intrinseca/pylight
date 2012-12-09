from console.attributes import RGBColorAttribute

class Red(RGBColorAttribute):
    def __init__(self):
        RGBColorAttribute.__init__(self, 255, 0, 0)

class White(RGBColorAttribute):
    def __init__(self):
        RGBColorAttribute.__init__(self, 255, 255, 255)
        
class Orange(RGBColorAttribute):
    def __init__(self):
        RGBColorAttribute.__init__(self, 255, 128, 0)
    