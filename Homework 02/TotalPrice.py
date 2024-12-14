# --------------------------------------------
# Divi Newton
# September 12, 2023
# Homework 02
#
# README
# This code asks the user to input the price of an item and outputs the price with tax added. 
# It converts the input to a float and then adds the price times the tax to find the total price. 
# -----------------------------------------------

print("Hello, welcome to the Total Price Calculator!")
ListPrice = input("Please enter the list price of your item: $ ")
ListPrice = (float(ListPrice))
TotalPrice = round(ListPrice + (ListPrice * 0.0725), 2)
print("The total price of your item is $",TotalPrice)