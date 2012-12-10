from console import Rig
from console.heads import Dimmer, FourChannelLED, ThreeChannelLED
import console.colors.rgb as colors
from interface import Terminal

r = Rig()

for i in range(1, 25):
    d = Dimmer(1, i)
    r.heads[i] = d
    d.attributes["MasterIntensity"].value = i * 10

#l1 = FourChannelLED(1, 33)
#l2 = ThreeChannelLED(1, 49)
#
#l1.intensity.value = 12
#l1.color = colors.Red()
#
#l2.intensity.value = 99
#l2.color = colors.Orange()

interface = Terminal(r)
interface.start()
