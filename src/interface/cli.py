import re

class CLI(object):
    def __init__(self, uni):
        self.uni = uni
    
    def parseLine(self, line):
        pattern = re.compile("^([\d]{1,3})(-([\d]{1,3}))?@([\d]{2,3})")
        m = pattern.match(line)
        if(m):
            startChan = int(m.group(1))
            value = int(m.group(4))
            
            if(m.group(3) == None):
                endChan = startChan
            else:
                endChan = int(m.group(3))
                
            for i in range(startChan - 1, endChan):
                self.uni.channels[i] = value
    
    
    
    



