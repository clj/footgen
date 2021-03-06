#!/usr/bin/python

from footgen import *

f = Footgen("gedatest", output_format="geda")
f.generator.clearance = 0.5
f.generator.mask_clearance = 0.2
f.qfn(pitch=0.5, pins=16, pinswide = 3, width=2.2, height = 2.5, padheight=0.254, padwidth=0.66, silk_xsize=3.0)
f.thermal_pad(1.66, pin=17)
f.via_array(columns=2, pitch=1.0, size=0.2, pad=0.5, pin = 17)
f.finish()
