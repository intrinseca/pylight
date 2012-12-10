from sys import stdin, stdout
from interface import parsers

class Terminal:
    def __init__(self, rig):
        self.rig = rig
        
    
    def start(self):
        self.parser = parsers.CLI(self.rig)
        
        while True:
            stdout.write("pyl> ")
            line = stdin.readline()
            
            self.parser.parseLine(line)
            
            self.rig.refresh()
            print self.rig.outputs[0]
            