# --------------------------------------------
# Divi Newton
# September 12, 2023
# Homework 02
# Dylan Ravel
#
# README
# This code takes the input of a tank's volume measurement and outputs the tank's footprint.
# The program does this by finding the side of the tank (through cube root) and then getting the area (through squaring). 
# -----------------------------------------------

import math
print("Hello, welcome to the Tank Measurement program")
VolumeL = float(input("Please enter the volume of the tank in liters: "))
Species = input("What type of reptile would you like to adopt? ")
VolumeCM = VolumeL * 1000
Side = math.pow(VolumeCM , 1/3)
Footprint = round(Side ** 2 , 2)
print("The bottom of your tank will have an area of", Footprint, "square centimeters.")
print("Your", Species, "will love that!!")