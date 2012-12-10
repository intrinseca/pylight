import copy

class State:
    def __init__(self):
        self.savedHeads = {}
        self.name = ""
    
    def save(self, sourceHeads):
        for headNumber, head in sourceHeads.iteritems():
            attrs = {}
            for key, attr in head.attributes.iteritems():
                attrs[key] = copy.deepcopy(attr)
            
            self.savedHeads[headNumber] = attrs
    
    def restore(self, targetHeads):
        for headNumber, attrs in self.savedHeads.iteritems():
            for key, attr in attrs.iteritems():
                targetHeads[headNumber].attributes[key] = copy.deepcopy(attr)
        