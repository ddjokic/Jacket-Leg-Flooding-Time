#!/usr/bin/env python
import inout
print("Calculating time to flood a jacket leg from diaphragm rupture")
print("Script downloaded long time ago and modified to my liking. Credits to (unknown) author") 
rb1 = inout.get_float("Input Reserve buoyancy - intact [t] or '0' for 50: ", 50)
rb2=inout.get_float("Input Reserve buoyancy - damaged [t] or '0' for 30: ",30)
rbt = (rb1+rb2)/2
n = inout.get_integer("Input number of jacket legs or '0' for 3: ", 3)
A=inout.get_float("Input Average area of rupture [sqm] or '0' for 0.25: ", 0.25)
Vol=inout.get_float("Input innel volume of jacket leg [cum] or '0' for 10: ", 10)
#Gravity acceleration
g = 9.81
#Seawater density (MN/m**3)
Y = 0.01025
E = 2.1E+5
#Average reserve buoyancy per jacket leg:
rb = rbt * g /n
# Y in kg/m^3
# Hydostatic head (m)
h = rb / (2.0 * g * Y * 1000.**2 / g)
# Velocity of water ingress (m/s)
V = (2. * g * h)**0.5
# Flow of water into the jacket leg (m^3/s)
Q = V * A
#Vol = input("Enter inner volume of the jacket leg (m^3): ")
# Time to flood jacket leg completely (s)
t = Vol / Q
print("Water flow into jacket leg [cum/s]: ", round (Q,3))
print ("Time to flood [hours]: ", round(t/3600., 3))