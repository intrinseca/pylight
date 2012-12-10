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
            
            self.parser.parseLine(line)
            
            print self.rig.outputs[0]
            