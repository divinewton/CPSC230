# -----------------------------------------------
# Divi Newton
# Collaborators: Dylan Ravel
# References: Google
# -----------------------------------------------

'''
1.  Using modulo, check whether 1069 is odd or even. Try this on a few different
    numbers. Can you use this idea to write an if-statement that tells the user if 
    their number is odd or even?
'''
print(1069%2)

num = int(input('Enter a number: '))
if num %2 == 0:
    print('Your number is even!')
else:
    print('Your number is odd!')

'''
2.  Ask the user for the radius of a circle. Use the full value of pi stored 
    in the math module to calculate the area and circumference of that circle 
    and display the results.
'''

import math
r = float(input("Enter the radius of a circle: "))
area = round(((math.pi * r) ** 2), 2)
circumference = round((2 * math.pi * r), 2)
print("Your circle with a radius of", r, "has an area of", area, "and a circumference of", circumference, "!!")

'''
3.  Write some code to tell the user whether or not to water their succulent. 
    You can prompt them with the question "Is the soil wet?". If they say "yes"
    print a statement telling them to leave it alone. If they say "no" print
    a statement telling them to water the plant
'''

wet = input('Is the soil wet? ')
if wet == "yes" or wet == "Yes":
    print('No need to water it!')
elif wet == "no" or "No":
    print('Time to water your plant!')
else:
    print('Try again with yes or no')

'''
4.  You can use the len() function to check the length of a collection type
    (ie numbers of characters in a string, individual items in a set, etc.).
    Ask the user to input a word and store it in the variable my_word. Using 
    len() and an if statement, write some code that checks whether the length 
    of a word is greater than or equal to 10. If it is, print out: 
    "Wow, that is a long word!"
'''

my_word = input("Enter a word: ")
if len(my_word) >= 10:
    print("Wow, that is a long word!")
else:
    print("That's a pretty small word...")