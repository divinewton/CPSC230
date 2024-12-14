# --------------------------------------------
# Divi Newton
# September 12, 2023
# Homework 02
#
# README
# This code asks the user to input the current temperature in Fahrenheit, and outputs the temperature converted into Celsius.
# It works by converting the temp to a float, and using the common celsius = (fahrenheit - 32) * 5 / 9 formula to output the answer.
# -----------------------------------------------

print("Hello, welcome to the Fahrenheit to Celsius Converter!")
TempF = input("Please enter the current temperature in degrees Fahrenheit: ")
TempF = (float(TempF))
TempC = round((TempF - 32) * 5 / 9, 2)
print("The current temperature in degrees Celsius is:",TempC)