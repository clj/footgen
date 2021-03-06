#!/usr/bin/python

from footgen import *

f = Footgen("LP3")
f.qfn(pitch=0.5, pins=16, width=2.2, padheight=0.254, padwidth=0.66, silk_xsize=3.0)
f.thermal_pad(1.66, pin=17)
f.via_array(columns=2, pitch=1.0, size=0.2, pad=0.5, pin = 17)
f.finish()

f = Footgen("MCL_DQ1225")
f.qfn(pitch = 0.5, pins = 12, width = 2.2, padheight = 0.25, padwidth = 0.55, silk_xsize = 3.0)
f.thermal_pad(1.3, pin=13)
f.via_array(columns=2, pitch=0.8, size=0.2, pad=0.5, pin=13)
f.finish()

f = Footgen("QFN48_7x7")
f.qfn(pitch = 0.5, pins = 48, width = 6.2, padheight = 0.254, padwidth = 0.60, silk_xsize = 7.0)
f.thermal_pad(5.1, pin=49)
f.via_array(columns=4, pitch=1.4, pin=49, pad=0.5, size=0.2)
f.finish()

f = Footgen("QFN40_6x6")
f.qfn(pitch = 0.5, pins = 40, width = 5.2, padheight = 0.254, padwidth = 0.60, silk_xsize = 6.0)
f.thermal_pad(3.8, pin=41)
f.via_array(columns=4, pitch=1.25, pin=41, pad=0.5, size=0.2, outer_only=True)
f.finish()

f = Footgen("QFN64_9x9")
f.qfn(pitch = 0.5, pins = 64, width = 8.2, padheight = 0.254, padwidth = 0.60, silk_xsize = 9.0)
f.thermal_pad(6.2, pin=65)
f.via_array(columns=5, pitch=1.4, pin=65, pad=0.5, size=0.2)
f.finish()

f = Footgen("QFN32_5x5")
f.qfn(pitch = 0.5, pins = 32, width = 4.15, padheight = 0.254, padwidth = 0.7, silk_xsize = 5.0)
f.thermal_pad(3.15, pin=33, copper_expansion = 0.3)
f.via_array(columns=6, pitch=0.65, size=0.2, pad=0.46, pin = 33, mask_clearance=-0.1, outer_only=True)
f.finish()

f = Footgen("QFN24_4x4")
f.qfn(pitch = 0.5, pins = 24, width = 3.2, padheight = 0.25, padwidth = 0.6, silk_xsize = 4.0)
f.thermal_pad(2.6, pin=25)
f.via_array(columns=3, pitch=1.0, size=0.2, pad=0.5, pin=25)
f.finish()

f = Footgen("QFN28_4x5")
f.qfn(pitch = 0.5, width=3.15, height=4.15, padheight=0.25, padwidth=0.7, pins = 28, pinswide = 6, silk_xsize = 4.0, silk_ysize = 5.0)
f.thermal_pad(w=2.6, h=3.6, pin=29, copper_expansion=0.1)
f.via_array(columns=5, rows=6, pitch=0.575, pitchy=0.665, size=0.2, pad=0.46, pin=29, mask_clearance=-0.1, outer_only=True)
f.finish()

f = Footgen("QFN20_5x5")
f.qfn(pitch = 0.65, pins = 20, width = 4.0, padheight = 0.35, padwidth = 0.7, silk_xsize = 5.0)
f.thermal_pad(3.15, pin=21)
f.via_array(columns=4, pitch=0.75, pin=21)
f.finish()

f = Footgen("PQFP48_7x7")
f.qfn(pitch = 0.5, pins = 48, width = 6.9, padheight = 0.3, padwidth = 1.5, silk_xsize = 7.0)
f.thermal_pad(6, pin=49, copper_expansion=0.3)
f.via_array(columns=5, pitch=1.2, size=0.3, pad=0.6, pin=49, mask_clearance = -0.1)
f.finish()

f = Footgen("qfn16_4x4")
f.qfn(pitch = 0.65, pins = 16, width = 3.1, padheight = 0.35, padwidth = 0.85, silk_xsize = 4.0)
f.thermal_pad(2.7, dots=[2,2])
f.via_array(columns=3, pitch=1.1, size=0.2, pad=0.5)
f.finish()
