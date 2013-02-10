import time
class State:    
    def __init__(self):
        self.fx = []
        self.savedHeads = {}
        self.name = ""
    
    def add_fx(self, head_numbers, fx):
        self.fx.append((head_numbers, fx))
        
    def apply(self, heads):
        t = time.time()
        for head_numbers, fx in self.fx:
            i = 0
            step = (t % fx.time) / fx.time
            
            for head_number in head_numbers:
                fx.apply(i, len(head_numbers), heads[head_number], step)
                i += 1