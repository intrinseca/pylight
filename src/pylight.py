from console import Rig, Show
from console.heads import Dimmer, FourChannelLED, ThreeChannelLED
import console.colors.rgb as colors
from interface import Terminal

r = Rig()
show = Show(r)

for i in range(1, 25):
    d = Dimmer(1, i)
    r.heads[i] = d
    d.attributes["MasterIntensity"].value = i * 10

show.saveState()

for i in range(1, 25):
    d = Dimmer(1, i)
    r.heads[i] = d
    d.attributes["MasterIntensity"].value = i * 5

show.saveState()

#l1 = FourChannelLED(1, 33)
#l2 = ThreeChannelLED(1, 49)
#
#l1.intensity.value = 12
#l1.color = colors.Red()
#
#l2.intensity.value = 99
#l2.color = colors.Orange()

interface = Terminal(show)
interface.start()
