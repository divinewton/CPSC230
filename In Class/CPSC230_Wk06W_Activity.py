# Divi Newton
# Collaborator: Dylan Ravel

'''
1.  Write a while loop asking students to enter the names of the classes
    they are taking this semester. They should be able to enter DONE when
    they have no classes to list. Each time they enter a class, print out
    "Wow, [Class Name], sounds fun!". If the class contains the word 
    "computer" (like CPSC 230: Computer Science 1) use string methods to 
    change the text to be entirely upper-case. (you can also modify to 
    highlight your own favorite topic other than "computer")
'''
className = input("Enter a class name (enter \"done\" if no more classes): ")
while True:
    if "done" not in className:
        if "computer" in className:
            print(f"Wow {className} sounds fun!".upper())
        else:
            print("Wow,", className, "sounds fun!")
        className = input("Enter a class name (enter \"done\" if no more classes): ")
    else:
        break

'''
2.  Ask the user to enter a number greater than 100 [userNum]. Include
    error handling in a while loop so that your script keeps asking 
    until the user enters an integer (using .isdigit()).
    
    Using another while loop and modulo, calculate the sum of all the 
    even numbers between 1 and [userNum]. Print out the sum.
    
    HINT: Look at the code you wrote using modulo (%) to determine if 
        a number was odd or even. (and look at the example code from 
        lecture today)
'''

userNum = input("Enter a number greater than 100: ")
while not userNum.isdigit():
    print("That's not a number!")
    userNum = input("Enter a number greater than 100: ")

sum = 0
number = 0
while number <= int(userNum):
    if number % 2 == 0:
        sum += number
    number += 1
print(sum)

'''
3.  Update this piece of code to meet the following paramaters: 
        - Ask the user to enter their own string
        - Use string methods to change the user's string so it only 
          contains lowercase letters and has no spaces at the start or end
        - Pick your own "favorite word" to highlight (mine is "Fish" in 
          the example below)
'''
i = 0
word = input("Enter a string: ")
word = word.lower().strip()
while i < len(word):
    print(word[i])
    if word[i] == "a":
        print("Apple starts with the letter A!")
        break
    else:
        i += 1
