import re

class CLI(object):    
    def __init__(self, show):
        self.show = show
        
        self.commands = [(re.compile("^([\d]{1,3})(-([\d]{1,3}))?@([\d]{2,3})"), self.setIntensity),
                         (re.compile("save"), self.save),
                         (re.compile("restore (\d+)"), self.restore),
                         (re.compile("seq( (\d+))?\r\n"), self.selectSequence),
                         (re.compile("seqadd (\d+)"), self.addStateToSequence)]
        
        self.currentSequence = None
    
    def save(self, matches):
        self.show.saveState()
        return "State {} saved".format(len(self.show.states))
    
    def restore(self, matches):
        index = int(matches.group(1))
        self.show.restoreState(self.show.states[index - 1])
        return "State {} restored".format(index)
        pass
    
    def setIntensity(self, matches):
        startHead = int(matches.group(1))
        value = int(matches.group(4))
        
        if(matches.group(3) == None):
            endHead = startHead
        else:
            endHead = int(matches.group(3))
        
        for i in range(startHead, endHead + 1):
            self.show.rig.heads[i].attributes["MasterIntensity"].value = value
    
    def selectSequence(self, matches):
        if matches.group(2) == None:
            self.show.sequences.append([])
            self.currentSequence = len(self.show.sequences) - 1
            return "Created Sequence {}".format(self.currentSequence + 1)
        else:
            self.currentSequence = int(matches.group(1)) - 1
            return "Selected Sequence {}".format(self.currentSequence + 1)
            
    
    def addStateToSequence(self, matches):
        state = int(matches.group(1)) - 1
        self.show.sequences[self.currentSequence].append(self.show.states[state])
    
    def parseLine(self, line):
        for regex, command in self.commands:
            m = regex.match(line)
            if m <> None:
                return command(m)
