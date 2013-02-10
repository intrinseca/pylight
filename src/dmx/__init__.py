class Universe(object):
    def __init__(self):
        self.channels = [0] * 512;
    
    def __str__(self):
        ret = ""
        columns = 16        
        fmt = " ".join(["{:3}"] * columns)
        i = 1
        
        for x in zip(*[iter(self.channels)] * columns):
            ret += "{:3}: ".format(i) + fmt.format(*x) + '\n'
            i += columns
        return ret

class Address:
    universe = 1
    channel = 1
    
    def __init__(self, uni, chan):
        assert(uni > 0)
        assert(chan >= 1 and chan <= 512)
        
        self.universe = uni
        self.channel = chan