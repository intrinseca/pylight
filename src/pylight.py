from console import Rig, Show
from console.heads import Dimmer
from interface import Terminal
from console import fx
from artnet import ArtNetSender
from twisted.internet import reactor

r = Rig()
show = Show(r)

for i in range(1, 9):
    d = Dimmer(1, i)
    r.heads[i] = d

f = fx.IntensityRamp()
show.programmer.add_fx(range(1, 9), f)
show.run()

artnet = ArtNetSender(r.outputs[0])

reactor.listenUDP(6454, artnet)
reactor.run()

interface = Terminal(show)
interface.start()
