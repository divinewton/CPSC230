'''Last Class'''
'''
1.  Work on your while loop from last class. If you need to, draw 
    your branching diagram back up on the board. If you make any 
    changes, re-upload a photo to Canvas. If you already wrote your
    loop, copy-paste it here. Add comments so I know what your loop
    is meant do do.
    
    NOTE: You can use the monitors at your tables to code together
'''

MoneyInBank = True # sets money in back to true
UserMoney = int(input("How much money is in your account? ")) # asks how much money
while MoneyInBank: 
    if UserMoney > 0: # if has money
        UserMoney -= 1 # removes some money
        print("You have money!") # prints "you have money"
    else: MoneyInBank = False # sets money to false
print("You're poor now") # tells user they're poor

'''Strings'''
'''
2.  Use a while loop to create a list of classes a student is taking.
        - Ask the user to enter the course code (e.g. CPSC 230)
        - If they enter a course code, print out "Cool! [course] sounds 
          like a fun class!"
        - If they enter an empty string, break the loop.
'''

Class = input("Enter course code: ")
while Class != "":
    print("Cool!", Class, "sounds like a fun class!")
    Class = input("Enter another course code: ")

'''
3.  Write some code that asks the user to input all the fish species they can name. 
        - If the user types "done," break out of the loop.
        - Otherwise, Add the species they've inputted to a string, my_fish, 
          that stores the species they've input so far (use the + operator).
        - If the word "fish" is in the name (ie "Clown Fish and Trigger Fish, 
          but not Eel or Trout), print out "Double Fish!"
        - Print out my_fish at the end.
'''
    
### EXAMPLE CODE ###
print("!" in "Hello!")  # this is True
print("He" in "Hello!") # this is True
print("HE" in "Hello")   # this is False
print(" " in "This is Boring.") # this is True
print(" " in "ThisIsBoring.")   # this is False

my_fish = "" # to keep track of inputs
End = False
Finish = "done"
while not End:
    FishInput = input("Enter fish species: ")
    if FishInput != Finish:
        if FishInput != "":
            if "Fish" in FishInput or "fish" in FishInput:
                print("Double Fish!")
                my_fish = my_fish + " " + FishInput 
            else:
                print("Type \'done\' to cancel.")
        else: 
          End = True
print(my_fish)

'''
4.  Grab and print the species "Clown Fish" from the following 
    strings using string slicing.
'''

s1 = "Clown Fish"
s2 = "Nemo is a Clown Fish"
s3 = "Dory is not a Clown Fish"
s4 = "FishClown" # hint [::]
s5 = "hsiF nwolC"
s6 = "hesmivFx wnnweoglmC"

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

# Hint: what will this print out?
y = "piUk pudolYj oeVvliPGm  alnlntokG  NreeJvWeON"
print(y[::-1])
print(y[::-2])

print(s1)
print(s2[-1,-10])
print(s3[-1,-10])