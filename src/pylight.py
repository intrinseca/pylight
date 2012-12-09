from console import Rig
from console.heads import Dimmer, FourChannelLED, ThreeChannelLED
import console.colors.rgb as colors

r = Rig()

d1 = Dimmer(1, 1)
d2 = Dimmer(1, 8)
d3 = Dimmer(1, 9)
d4 = Dimmer(1, 256)

l1 = FourChannelLED(1, 33)
l2 = ThreeChannelLED(1, 49)

r.heads.append(d1)
r.heads.append(d2)
r.heads.append(d3)
r.heads.append(d4)
r.heads.append(l1)
r.heads.append(l2)

d1.intensity.value = 45
d2.intensity.value = 46
d3.intensity.value = 47
d4.intensity.value = 255

l1.intensity.value = 12
l1.color = colors.Red()

l2.intensity.value = 99
l2.color = colors.Orange()

r.refresh()

print r.outputs[0]