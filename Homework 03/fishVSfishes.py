# --------------------------------------------
# Divi Newton
# October 5, 2023
# Homework 03
#
# README
# This code asks the user to input three individual fish names, and lets the user know whether to use "fish" or "fishes" as their plural.
# It adds the names to a set and uses an if statement with len to determine if the names are the same. 
# If they are all the same, it outputs "fish," if not, it outputs "fishes."
# -----------------------------------------------

print("Hello, welcome to fish vs. fishes!")
fish1 = input("Enter an individual fish: ")
fish2 = input("Enter a second individual fish: ")
fish3 = input("Enter a third individual fish: ")
fishSet = {fish1, fish2, fish3}
if len(fishSet) == 1:
    print("Use \"fish\" when dicribing these fish!")
else:
    print("Use \"fishes\" when discribing these fishes!")