from console import Rig, Show
from console.heads import Dimmer, FourChannelLED, ThreeChannelLED
import console.colors.rgb as colors
from interface import Terminal
from console import fx

r = Rig()
show = Show(r)

for i in range(1, 25):
    d = Dimmer(1, i)
    r.heads[i] = d

interface = Terminal(show)
interface.start()
