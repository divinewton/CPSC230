'''
1.  Use this space to test out your answers for the quiz. Use 
    comments to make notes about how you answered the question 
    and/or what concepts you would like to focus on in preparation 
    for the midterm.
'''
### Practice Question 1

num01 = 1 + 1 #int
num02 = 10 / 5 #float
num03 = 10 // 5 #int
num04 = 1 * 2.0 #float
num05 = 10 % 8 #int

print(type(num01))
print(type(num02))
print(type(num03))
print(type(num04))
print(type(num05))

### Practice Question 2

userAnswer = input("How many classes are you taking?")
userAnswer = int(userAnswer) #convert to int from string
if userAnswer > 0 and userAnswer <= 3: #add userAnswer after and, and add ":"
    print("That sounds pretty manageable.")
elif userAnswer == 4: #add ":"
    print("Cool, me too!")
elif userAnswer >= 5: #add ":""
    print("Wow, you must be busy!")

### Practice Question 3

bestGame = {"Title": "Minecraft", "Character": "Steve", "Platform": "Xbox"}
if len(bestGame["Title"]) >= 10:
    print("Wow, that's a long name!")
elif len(bestGame["Title"]) < 10:
    print("Cool, sounds fun!")

''' 
2.  Emojis. Use pip install to install the emojis library.
        To install: pip install emojis

    Use it to print a short story in the terminal where every
    noun is replaced by an emoji.
        https://www.webfx.com/tools/emoji-cheat-sheet/

    If you are having issues with pip, you may need to reinstall
    follow instructions here: https://realpython.com/what-is-pip/
'''

import emojis
emojified = emojis.encode("There is a :snake: in my boot !")
print(emojified)

emojiStory = emojis.encode(":selfie::woman_dancing::mirror_ball: :musical_note:")
print(emojiStory)

'''
3.  Find, install, and use one other library of your choosing.
    You can just google "interesting libraries in python"

    NOTE: It is normal to have issues installing libraries. Python
    is open-source, so sometimes working with less commonly used 
    libraries is a pain. It's not you! Google is your friend here. 
'''