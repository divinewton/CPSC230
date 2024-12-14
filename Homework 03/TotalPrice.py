# --------------------------------------------
# Divi Newton
# October 5, 2023
# Homework 03
#
# README
# This code asks the user to input the price of an item and outputs the price with tax added. 
# It uses a while loop to ensure the entered value is a number and is above zero. 
# It then adds the price times the tax to find the total price and outputs the value.
# -----------------------------------------------

print("Hello, welcome to the Total Price Calculator!")
ListPrice = input("Please enter the list price of your item: $ ")
while True:
    if ListPrice.isdigit() and float(ListPrice) > 0:
        ListPrice = float(ListPrice)
        break
    else:
        print("That's not a valid price!")
        ListPrice = input("Enter a valid amount: $ ")
TotalPrice = round(ListPrice + (ListPrice * 0.0725), 2)
print("The total price of your item is $",TotalPrice)