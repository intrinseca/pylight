from twisted.internet.protocol import DatagramProtocol
import struct
from twisted.internet.task import LoopingCall

HEADER = 'Art-Net\0'
PROTOCOL_VERSION = 14

ARTNET_PORT = 6454

def lohi(i):
    low = i & 0x00FF
    high = (i & 0xFF00) >> 8
    return low, high

class ArtNetSender(DatagramProtocol):
    def __init__(self, universe):
        self.sequence = 1     
        self.universe = universe
    
    def startProtocol(self):
        self.send_timer = LoopingCall(self.send)
        self.send_timer.start(0.1)
        
    def send(self):
        proto_lo, proto_hi = lohi(14)
        len_lo, len_hi = lohi(512)
        header = struct.pack('!8sHBBBBHBB', 
                             HEADER, 0x0050, proto_hi, proto_lo,
                             self.sequence, 0, 0, len_hi, len_lo)
        packet = header + ''.join([struct.pack('!B', c) for c in self.universe.channels])
        self.transport.write(packet, ('192.168.1.43', ARTNET_PORT))
        
        if self.sequence == 0xFF:
            self.sequence = 1
        else:
            self.sequence += 1
    
    def datagramReceived(self, data, (host, port)):
        pass