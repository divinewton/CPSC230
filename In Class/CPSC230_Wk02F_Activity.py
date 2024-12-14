# Class Activities Week 2 - Friday

# Classwork-----------------------------------------------
'''
1.  Use Python to change z into a string. Display the type(z) in the terminal
    before and after making the change.
'''
print("--- Problem 1 ---")

z = 156
print(type(z))
x = str(z)
print(type(x))

'''
2.  Write some code that asks the user to guess a number between 1-10.
    Convert that number to an int, and then a use boolean operation to
    check if the number they guessed is 7 (no if-statements required). 
    Print out the resulting Boolean value (True when they guessed 7, 
    and False otherwise.)
'''
print("--- Problem 2 ---")

Num = input("Guess a number between 1 and 10 ")
NewNum = int(Num)
print(NewNum == 7)

'''
3.  With your group, discuss why this code doesn't work, and what
    would need to be changed to fix it. Add comments to explain 
    what you did.
'''
print("--- Problem 3 ---")

i = int(input("How many times do you eat off campus each week? "))
avg = i/7
print(avg, " times a day on average! Cool!")
# you cannot divide a string by an int

'''
4.  Ask the user to enter a number, then use the math module to
    calculate the square root of that number and print out the result
'''
print("--- Problem 4 ---")

import math
x = int(input("Enter a number "))
y = math.sqrt(x)
print("The square root of ", x , "is ", y)

'''
5.  Pull up the code from the Week 2 - Wednesday activity. Let's make
    the triangle area calculator more interactive. Instead of simply
    defnining x and y yourself, ask the user to enter two numbers (b, h)
    to represent the base and hight of their triangle. Display the result 
    to the user (ex. "The area of your triangle is 15")
'''
print("--- Problem 5 ---")

b = int(input('Enter triangle base '))
h = int(input('Enter triangle height '))
area = (b * x)/2
print("The area of the triangle is", area, "!")

'''
6.  BONUS: Chat with your group about other useful equations you could run using
    input from a user (area of a circle, a backyard, etc.). Make a plan and
    write a small chunk of code that takes at least 2 user inputs and 
    displays the result of at least 1 calculation. Feel free to use the 
    monitors at your tables and work together.
'''
print("--- Problem 6 ---")

b = int(input("Enter a number "))
h = int(input("Enter a second number "))
area = b * h
print ("The area of a rectangle with sides", b , "and", h , "is", area, "!!")