# Class Activities

'''For Loop Example'''
pie = ["butter", "flour", "apples", "sugar"]

for food in pie:
    if food == "apple":
        print(food, ": those you need to pick yourself")
    else:
        print(food, ": that you can get at the store")

# Classwork-----------------------------------------------
'''
1.  Make a list the classes you are taking this semester, then use a 
    for loop which loops throgh the list and prints out "[Class Name] 
    is one of my favotite classes!" for each class containing the word
    "computer" and "[Class Name] sounds like fun!" for all other classes.
'''
CourseTitles = ["Computer Science 1", "Computer Science Colloquium", "FFC Grand Challenges", "Math 101", "Engineering 101"]
for course in CourseTitles:
    if "Computer" in course:
        print(course, "is one of my favorite classes!")
    else:
        print(course, "sounds like fun!")

'''
2.  Ask a user to input a positive integer. If they enter a float, 0, or 
    a negative number (use isdigit()), keep asking (use a while loop).
    
    Once you have their number, calculate the factorial (see: 
    https://en.wikipedia.org/wiki/Factorial)for each number from 1 to that 
    number, and print it out (HINT, use range()).

    To test it, the answer for 5 is 120
'''
UserNum  = input("Enter a positive integer: ")
while not UserNum.isdigit() or int(UserNum) <= 0:
    print("That's not a valid integer.")
    UserNum = input("Enter a valud integer: ")

factorial = 1

for i in range(1, int(UserNum) + 1):
    factorial *= i
print("The factorial of", UserNum, "is", factorial)

'''
3.  Ask the user to enter a number greater than 100 [userNum]. Include
    error handling so that your script keeps asking until the user enters
    an integer (using .isdigit()).
    
    Using a for loop, an if statement, and range(), calculate the sum 
    of all the even numbers between 1 and [userNum]. Print out the sum.
    
    HINT: Look at the code you wrote using modulo (%) to determine if a 
        number was odd or even.
    
    To test it, the answer for 110 is 3080
'''
userNum = input("Enter a number greater than 100: ")
while not userNum.isdigit() or int(userNum) <= 100:
    print("That's not a number over 100.")
    userNum = input("Enter a number greater than 100: ")

for i in userNum:
    range(1, int(userNum), 2)

'''
4.  Update this piece of code to meet the following paramaters: 
        - Re-write the while loop as a for loop
        - Ask the user to enter their own string
        - Change the user's string so it only contains lowercase letters 
          and has no spaces at the start or end using string methods
        - Pick your own "favorite word" to highlight (mine is "Fish" in 
          the example below)
'''
i = 0
word = "If I were a fish..."
while i < len(word):
    print(word[i])
    if word[i] == "f":
        print("Fish starts with the letter F!")
        break
    else:
        i += 1


'''
5.  Start working on your project.

    Create the "Start of game" section which establishes the chacacter
    dictionaries and asks the user to choose their character. You can
    edit this later of course, but try and outline it now.
'''

PC1 = {"type": "dog", "health": 100, "attack": 50, "dodge": 0.5}
PC2 = {"type": "cat", "health": 75, "attack": 75, "dodge": 0.25}
NPC = {"type": "bird", "health": 50, "attack": 100, "dodge": 0.75}

print("Welcome to the game!")
print("Your character options are", PC1["type"], "and", PC2["type"], "!")