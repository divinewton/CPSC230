# -----------------------------------------------
# Divi Newton
# November 3, 2023
# Project Part 2
# ----------------------------------------------------

import random # imports ramdom library
# dictionaries containing player and NPC types, health, attack modifiers, attack dice, and dodge dice:
PC1 = {"PlayerType": "Dog", "Health": 100, "AttackMod": 35, "AttackDice": 10, "DodgeDice": 8}
PC2 = {"PlayerType": "Cat", "Health": 150, "AttackMod": 20, "AttackDice": 8, "DodgeDice": 12}
PC3 = {"PlayerType": "Fish", "Health": 70, "AttackMod": 10, "AttackDice": 5, "DodgeDice": 8}
PC4 = {"PlayerType": "Pig", "Health": 100, "AttackMod": 25, "AttackDice": 6, "DodgeDice": 8}
PC5 = {"PlayerType": "Goat", "Health": 80, "AttackMod": 20, "AttackDice": 6, "DodgeDice": 10}
NPC1 = {"PlayerType": "Bird", "Health": 75, "AttackMod": 10, "AttackDice": 8, "DodgeDice": 8}
NPC2 = {"PlayerType": "Raccoon", "Health": 100, "AttackMod": 30, "AttackDice": 10, "DodgeDice": 10}
NPC3 = {"PlayerType": "Panther", "Health": 200, "AttackMod": 40, "AttackDice": 14, "DodgeDice": 12}
# welcome to the game and name assignment:
print("Welcome to the combat game!")
PlayerName = input("Enter your name: ")
PlayerName = PlayerName.strip().title()
# assigning character:
print("Welcome " + PlayerName + "! Choose a player to begin!")
print("Your character options are: ") # character options for PC
print(PC1["PlayerType"], "with", PC1["Health"], "starting health,", PC1["AttackMod"], "minimum attack,", PC1["AttackDice"], "attack dice, and", PC1["DodgeDice"], "dodge dice")
print(PC2["PlayerType"], "with", PC2["Health"], "starting health,", PC2["AttackMod"], "minimum attack,", PC2["AttackDice"], "attack dice, and", PC2["DodgeDice"], "dodge dice")
print(PC3["PlayerType"], "with", PC3["Health"], "starting health,", PC3["AttackMod"], "minimum attack,", PC3["AttackDice"], "attack dice, and", PC3["DodgeDice"], "dodge dice")
print(PC4["PlayerType"], "with", PC4["Health"], "starting health,", PC4["AttackMod"], "minimum attack,", PC4["AttackDice"], "attack dice, and", PC4["DodgeDice"], "dodge dice")
print(PC5["PlayerType"], "with", PC5["Health"], "starting health,", PC5["AttackMod"], "minimum attack,", PC5["AttackDice"], "attack dice, and", PC5["DodgeDice"], "dodge dice")
Character = input("Please choose an option to continue: ") # user is asked to enter a player choice after seeing the options
Character = Character.strip()
# ensures correct character entered, assigns character PC variable:
while True: 
    if Character.lower() == "dog" or Character.lower() == "cat" or Character.lower() == "fish" or Character.lower() == "pig" or Character.lower() == "goat":
        if Character.lower() == "dog": # if they enter dog, PC is set to PC1
            PC = PC1
            break
        elif Character.lower() == "cat": # if they enter cat, PC is set to PC2
            PC = PC2
            break
        elif Character.lower() == "fish": # if they enter fish, PC is set to PC3
            PC = PC3
            break
        elif Character.lower() == "pig": # if they enter pig, PC is set to PC4
            PC = PC4
            break
        elif Character.lower() == "goat": # if they enter goat, PC is set to PC5
            PC = PC5
            break
    else:
        print("You entered an incorrect player.") # if entered an incorrect player, prompted again 
        Character = input("Please choose one of the given options to continue: ")
        Character = Character.strip()
# choosing the opponent:
print("Now it's time to choose and opponent!\nWould you like to choose the opponent yourself or let the computer decide?")
NPCChoice = input("Enter \"choose\" if you would like to choose, or \"random\" if you would like the computer to choose for you: ")
NPCChoice = NPCChoice.strip()
isChoosing = True
while isChoosing:
    if NPCChoice.lower() == "choose": # if the user chooses to choose their opponent
        print("Your opponent options are:") # opponent options
        print(NPC1["PlayerType"], "with", NPC1["Health"], "starting health,", NPC1["AttackMod"], "minimum attack,", NPC1["AttackDice"], "attack dice, and", NPC1["DodgeDice"], "dodge dice")
        print(NPC2["PlayerType"], "with", NPC2["Health"], "starting health,", NPC2["AttackMod"], "minimum attack,", NPC2["AttackDice"], "attack dice, and", NPC2["DodgeDice"], "dodge dice")
        print(NPC3["PlayerType"], "with", NPC3["Health"], "starting health,", NPC3["AttackMod"], "minimum attack,", NPC3["AttackDice"], "attack dice, and", NPC3["DodgeDice"], "dodge dice")
        Choice = input("Please choose an option to continue: ")
        Choice = Choice.strip()
        while True: # assigns chosen NPC with the NPC variabl and ensures a correct opponent answer was given
            if Choice.lower() == "bird" or Choice.lower() == "raccoon" or Choice.lower() == "panther":
                if Choice.lower() == "bird": # if they enter bird, NPC is set to NPC1
                    NPC = NPC1
                    isChoosing = False # breaks both loops
                    break
                elif Choice.lower() == "raccoon": # if they enter raccoon, NPC is set to NPC2
                    NPC = NPC2
                    isChoosing = False # breaks both loops
                    break
                elif Choice.lower() == "panther": # if they enter panther, NPC is set to NPC3
                    NPC = NPC3
                    isChoosing = False # breaks both loops
                    break
            else:
                print("You entered an incorrect NPC option.") # if entered an incorrect NPC, prompted again 
                Choice = input("Please choose \"bird,\" \"raccoon,\" or \"panther\" to continue: ")
                Choice = Choice.strip()
    elif NPCChoice.lower() == "random": # if the user chooses random
        RandNum = random.randint(0, 2) # chooses random number (between 0 and 2)
        if RandNum == 0:
            NPC = NPC1 # if the number is 0, NPC is NPC1
            break
        elif RandNum == 1:
            NPC = NPC2 # if the number is 1, NPC is NPC2
            break
        elif RandNum == 2:
            NPC = NPC3 # if the number is 2, NPC is NPC3
            break
    else:
        print("You entered an incorrect option.") # if entered an incorrect option, prompted again 
        NPCChoice = input("Enter \"choose\" if you would like to choose, or \"random\" if you would like the computer to choose for you: ")
        NPCChoice = NPCChoice.strip()
# states user and NPC players:
print("You chose", PC["PlayerType"], "with", PC["Health"], "starting health as your player. You will be playing against", NPC["PlayerType"], "with", NPC["Health"], "starting health.") # prints the chosen player and NPC with health stats
# defining the dice rolling function
def DiceRoll(integer):
    result = random.randint(1, integer) # random number between 1 and the input
    return result
# defining the damage function
def Damage(Attacker):
    RollResult = DiceRoll(Attacker["AttackDice"]) # the dice roll based on the player's attack dice in their dictionary
    AttempDamage = RollResult + Attacker["AttackMod"] # added the attack mod of that player
    return AttempDamage
# defining the dodge function
def Dodge(Dodger):
    DodgeNum = DiceRoll(Dodger["DodgeDice"]) # takes dice roll of the dice dodge of that player
    return DodgeNum
# starting the game: 
print("Let's get started, " + PlayerName + "!")
RoundNum = 1 # sets round number of the game
# playing the game:
while PC["Health"] > 0 and NPC["Health"] > 0: # ensured both players still hahe health
    print("---------- ROUND", RoundNum, "---------")
    PCAction = input("Do you want to Attack or Dodge? ")
    # ensure input in a valid action: attack or dodge:
    PCAction = PCAction.strip()
    while True: 
        if PCAction.lower() == "attack" or PCAction.lower() == "dodge":
            break
        else:
            print("You entered an incorrect action.") # ensured action was entered correctly
            PCAction = input("Please choose \"Attack\" or \"Dodge\" to continue: ")
            PCAction = PCAction.strip()
    PCAction = PCAction.title()
    # assigns NPC with a random action:
    RandNum = random.randint(0, 1) # chooses random number (either 0 or 1)
    if RandNum == 1:
        NPCAction = "Attack" # if the number is 1, NPC attacks
    elif RandNum == 0:
        NPCAction = "Dodge" # if the number is 0, NPC dodges
    # outcome of the round:
    print("You chose to", PCAction, "and your opponent chose to", NPCAction) # prints both players action choices
    # if PC chose attack and NPC also chose attack:
    if PCAction == "Attack" and NPCAction == "Attack": 
        PC["Health"] -= Damage(NPC) # PC health is PC health minus NPC attack through the damage function
        NPC["Health"] -= Damage(PC) # NPC health is NPC health minus PC attack through the damage function
        PCDamage = Damage(NPC) # PC damage is NPC through the damage function
        NPCDamage = Damage(PC) # NPC damage is PC through the damage function
    # if PC chose attack and NPC chose dodge:
    elif PCAction == "Attack" and NPCAction == "Dodge": 
        NPC["Health"] -= (Damage(PC) - Dodge(NPC)) # NPC health is NPC health minus PC attack through the damage function - NPC through the dodge function
        PCDamage = 0 # PC damage is none
        NPCDamage = Damage(PC) - Dodge(NPC) # NPC damage is PC damage through damage function - NPC through the dodge function
    # if PC chose dodge and NPC chose attack:
    elif PCAction == "Dodge" and NPCAction == "Attack":
        PC["Health"] -= Damage(NPC) - Dodge(PC) # PC health is PC health minus NPC attack through the damage function - PC through the dodge function
        PCDamage = Damage(NPC) - Dodge(PC) # PC damage is NPC damage through damage function - PC through the dodge function
        NPCDamage = 0 # NPC damage is none
    # if PC chose dodge and NPC also chose dodge:
    elif PCAction == "Dodge" and NPCAction == "Dodge":
        PCDamage = 0 # PC damage is none
        NPCDamage = 0 # NPC damage is none
    # ensures doesn't display negetive health numbets
    if PC["Health"] < 0:
        PC["Health"] = 0
    elif NPC["Health"] < 0:
        NPC["Health"] = 0
    # print results of the round
    print("Your character,", PC["PlayerType"], "took", PCDamage, "damage, and your opponent", NPC["PlayerType"], "took", NPCDamage, "damage") # prints round damage
    print("Your current health is", PC["Health"], "and your opponent's health is", NPC["Health"]) # prints current PC and NPC health
    # iterate round number
    RoundNum += 1
print("---------- GAME OVER! ---------")
if NPC["Health"] <= 0 and PC["Health"] <= 0: # if both are under or equal to 0 health
    print("You tied. Both characters ended with 0 health.") # prints tied game
    print("Thank you for playing, " + PlayerName + ", we hope you'll play again soon!")
elif PC["Health"] <= 0: # if PC health is under or equal to 0
    print("You lost. Your opponent", NPC["PlayerType"], "finished with", NPC["Health"], "health.") # prints player lost the game
    print("Better luck next time, " + PlayerName + ", we hope you'll play again soon!")
elif NPC["Health"] <= 0: # if NPC health is under or equal to 0
    print("You Won! Your character", PC["PlayerType"], "finished with", PC["Health"], "health.") # prints player won the game!
    print("Thank you for playing, " + PlayerName + ", we hope you'll play again soon!")