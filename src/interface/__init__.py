from sys import stdin, stdout
from interface import parsers

class Terminal:
    def __init__(self, show):
        self.show = show
        
    
    def start(self):
        self.parser = parsers.CLI(self.show)
        
        while True:
            stdout.write("pyl> ")
            line = stdin.readline()
            
            response = self.parser.parseLine(line)
        
            if response:
                print "   ! " + response
            
            self.show.refresh()            
            print self.show.rig.outputs[0]
            