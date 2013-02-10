class State:    
    def __init__(self):
        self.fx = []
        self.savedHeads = {}
        self.name = ""
    
    def addFX(self, head_numbers, fx):
        self.fx.append((head_numbers, fx))
        
    def apply(self, heads):
        for head_numbers, fx in self.fx:
            i = 0
            for head_number in head_numbers:
                fx.apply(i, heads[head_number], 0)
                i += 1
        