# --------------------------------------------
# Divi Newton
# October 5, 2023
# Homework 03
#
# README
# This code asks the user to input the current temperature in Fahrenheit, and outputs the temperature converted into Celsius.
# It first uses a while loop to ensure the entered value is a number and is within known earth temperatures (between -130 and 135 Fahrenheit)
# It then uses the common celsius = (fahrenheit - 32) * 5 / 9 formula to output the answer to the user. 
# -----------------------------------------------

print("Hello, welcome to the Fahrenheit to Celsius Converter!")
TempF = input("Please enter the current temperature in degrees Fahrenheit: ")
while True:
    if TempF.isdigit() and float(TempF) > -130 and float(TempF) < 134:
        TempF = float(TempF)
        break
    else:
        print("That's not a valid temperature!")
        TempF = input("Enter a valid temperature in Fahrenheit: ")
TempC = round((TempF - 32) * 5 / 9, 2)
print("The current temperature in degrees Celsius is:",TempC)