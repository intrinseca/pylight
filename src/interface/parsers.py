import re

class CLI(object):
    def __init__(self, rig):
        self.rig = rig
    
    def parseLine(self, line):
        pattern = re.compile("^([\d]{1,3})(-([\d]{1,3}))?@([\d]{2,3})")
        m = pattern.match(line)
        
        if(m):
            startHead = int(m.group(1))
            value = int(m.group(4))
            
            if(m.group(3) == None):
                endHead = startHead
            else:
                endHead = int(m.group(3))
                
            for i in range(startHead, endHead + 1):
                self.rig.heads[i].attributes["MasterIntensity"].value = value
        
        self.rig.refresh()
