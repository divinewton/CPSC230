'''
1.  Guessing Game. Remember when we asked the user to guess a number and used 
    booleans to tell them if they were correct (see Wk02F_Activity)? Let's 
    make our game more interactive! 

    - First, create a number that will be the answer (answer = 7)
    - Second, create a counter variable to represent userAnswer (userAnswer = 0)
    - Then, create a while loop that repeatedly asks the user to guess a
      number between 1-10. The loop should only stop when userAnswer == answer
    - Congratulate the user when the loop ends (ie when they guess correctly)
'''

answer = 7
userAnswer = int(input("Enter a number between 0 and 10: "))
while userAnswer != answer:
    print("Nope!")
    userAnswer = int(input("Try a different number: "))
print("You got it!")

'''
2.  Modify your code above to keep track of how many guesses it takes the 
    user to get the correct answer. Be sure to display their guess count
    when they finally get it right!
'''

answer = 7
guessNumber = 1
userAnswer = int(input("Enter a number between 0 and 10: "))
while userAnswer != answer:
    print("Nope!")
    guessNumber = guessNumber + 1
    userAnswer = int(input("Try a different number: "))
print("You got it! It took you", guessNumber, "tries.")

'''
3.  Modify your code again so that you can play the game yourself! This 
    will require you to use the randint() function in the random module:
    https://docs.python.org/3/library/random.html#module-random
'''

import random
answer = random.randrange(1,11)
guessNumber = 1
userAnswer = int(input("Enter a number between 0 and 10: "))
while userAnswer != answer:
    print("Nope!")
    guessNumber = guessNumber + 1
    userAnswer = int(input("Try a different number: "))
print("You got it! It took you", guessNumber, "tries.")

'''
4.  Modify your code one last time. This time, use and/or statements to
    limit the number of guesses the user has to 5. If the user does not
    guess correctly after 5, tell them "Sorry, better luck next time!" 
    If the user does guess correctly, tell them "Nice work! You guessed
    the rignt number in X tries!" (where X is the number of guesses)
'''

import random
answer = random.randrange(1,11)
maxGuess = 5
guessNumber = 1
userAnswer = int(input("Enter a number between 0 and 10: "))
while userAnswer != answer and guessNumber < maxGuess:
    print("Nope!")
    guessNumber = guessNumber + 1
    userAnswer = int(input("Try a different number: "))
if guessNumber == maxGuess:
    print("Better luck next time!")
else:
    print("You got it! It took you", guessNumber, "tries.")