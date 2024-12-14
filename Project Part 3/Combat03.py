# -----------------------------------------------
# Divi Newton
# November 24, 2023
# Project Part 3
# ----------------------------------------------------

import random # imports ramdom library
print("Welcome to the combat game!") # welcome to the game
# begin transcript
filename = input("What would you like the game transcript file to be named? ")
transcript = open(filename + ".csv", "w")
transcript.write("---------- Combat Game Transcript ----------\n\n")
transcript.close()
# transcript function defined:
def transcription(textinput):
    transcript = open(filename + ".csv", "a")
    transcript.write(textinput)
    transcript.close()
# defining the dice rolling function
def DiceRoll(integer):
    result = random.randint(1, integer) # random number between 1 and the input
    return result
# defining character class
class CharacterOption():
    def __init__(self, PlayerType, Health, AttackMod, AttackDice, DodgeDice):
        self.PlayerType = PlayerType
        self.Health = Health
        self.AttackMod = AttackMod
        self.AttackDice = AttackDice
        self.DodgeDice = DodgeDice
    def Attack(self):
        RollResult = DiceRoll(self.AttackDice) # the dice roll based on the character's attack dice
        Damage = RollResult + self.AttackMod # added the attack mod to dice result
        return Damage
    def Dodge(self):
        SubDamage = DiceRoll(self.DodgeDice)
        return SubDamage
# creating 5 PC characters and 3 NPC characters:
PC1 = CharacterOption("Dog", 100, 35, 10, 8)
PC2 = CharacterOption("Cat", 150, 20, 8, 12)
PC3 = CharacterOption("Fish", 70, 10, 5, 8)
PC4 = CharacterOption("Pig", 100, 25, 6, 8)
PC5 = CharacterOption("Goat", 80, 20, 6, 10)
NPC1 = CharacterOption("Bird", 75, 10, 8, 8)
NPC2 = CharacterOption("Raccoon", 100, 30, 10, 10)
NPC3 = CharacterOption("Panther", 200, 40, 14, 12)
# name assignment:
PlayerName = input("Enter your name: ")
PlayerName = PlayerName.strip().title()
transcription("User Name: " + PlayerName + "\n\n")
# assigning character:
print("Welcome " + PlayerName + "! Choose a player to begin!")
print("Your character options are: ") # character options for PC
print(PC1.PlayerType + " (Health: " + str(PC1.Health) + ", Minimum Attack: " + str(PC1.AttackMod) + ", Attack Dice: " + str(PC1.AttackDice) + ", Dodge Dice: " + str(PC1.DodgeDice) + ")")
print(PC2.PlayerType + " (Health: " + str(PC2.Health) + ", Minimum Attack: " + str(PC2.AttackMod) + ", Attack Dice: " + str(PC2.AttackDice) + ", Dodge Dice: " + str(PC2.DodgeDice) + ")")
print(PC3.PlayerType + " (Health: " + str(PC3.Health) + ", Minimum Attack: " + str(PC3.AttackMod) + ", Attack Dice: " + str(PC3.AttackDice) + ", Dodge Dice: " + str(PC3.DodgeDice) + ")")
print(PC4.PlayerType + " (Health: " + str(PC4.Health) + ", Minimum Attack: " + str(PC4.AttackMod) + ", Attack Dice: " + str(PC4.AttackDice) + ", Dodge Dice: " + str(PC4.DodgeDice) + ")")
print(PC5.PlayerType + " (Health: " + str(PC5.Health) + ", Minimum Attack: " + str(PC5.AttackMod) + ", Attack Dice: " + str(PC5.AttackDice) + ", Dodge Dice: " + str(PC5.DodgeDice) + ")")
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
print("Now it's time to choose an opponent!\nWould you like to choose the opponent yourself or let the computer decide?")
NPCChoice = input("Enter \"choose\" if you would like to choose, or \"random\" if you would like the computer to choose for you: ")
NPCChoice = NPCChoice.strip()
isChoosing = True
while isChoosing:
    if NPCChoice.lower() == "choose": # if the user chooses to choose their opponent
        print("Your opponent options are:") # opponent options
        print(NPC1.PlayerType + " (Health: " + str(NPC1.Health) + ", Minimum Attack: " + str(NPC1.AttackMod) + ", Attack Dice: " + str(NPC1.AttackDice) + ", Dodge Dice: " + str(NPC1.DodgeDice) + ")")
        print(NPC2.PlayerType + " (Health: " + str(NPC2.Health) + ", Minimum Attack: " + str(NPC2.AttackMod) + ", Attack Dice: " + str(NPC2.AttackDice) + ", Dodge Dice: " + str(NPC2.DodgeDice) + ")")
        print(NPC3.PlayerType + " (Health: " + str(NPC3.Health) + ", Minimum Attack: " + str(NPC3.AttackMod) + ", Attack Dice: " + str(NPC3.AttackDice) + ", Dodge Dice: " + str(NPC3.DodgeDice) + ")")
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
# states user and NPC players, saves to transcript:
print("You chose", PC.PlayerType, "with", PC.Health, "starting health as your player. You will be playing against", NPC.PlayerType, "with", NPC.Health, "starting health.") # prints the chosen player and NPC with health stats
transcription(PC.PlayerType + " (PC) vs. " + NPC.PlayerType + " (NPC)\n")
# defines Print Results function:
def PrintResults(PC, NPC, PCDamage, NPCDamage, PCHealth, NPCHealth, NPCAttackMod, NPCAttackDice, PCAttackMod, PCAttackDice): # takes in variables
    print(PC + " took " + str(PCDamage) + " damage. Remaining health: " + str(PCHealth)) # prints PC damage and health
    print(NPC + " took " + str(NPCDamage) + " damage. Remaining health: " + str(NPCHealth)) # prints NPC damage and health
    if PCDamage == NPCAttackMod + NPCAttackDice:
        print("NPC rolled max damage!")
    if NPCDamage == PCAttackMod + PCAttackDice:
        print("PC rolled max damage!")
    if PCDamage == NPCAttackMod + 1:
        print("NPC rolled minimum damage.")
    if NPCDamage == PCAttackMod + 1:
        print("PC rolled minimum damage.")
    transcription(PC + " damage: " + str(PCDamage) + "\n" + NPC + " damage: " + str(NPCDamage) + "\n" + PC + " health: " + str(PCHealth) + "\n" + NPC + " health: " + str(NPCHealth) + "\n") # adds to transcript
# starting the game: 
print("Let's get started, " + PlayerName + "!")
RoundNum = 1 # sets round number of the game
# playing the game:
while PC.Health > 0 and NPC.Health > 0: # ensured both players still hahe health
    print("---------- ROUND", RoundNum, "---------")
    transcription("\n---------- Round #" + str(RoundNum) + " ----------\n") # adds round to transcript
    PCAction = input("Choose your action (attack or dodge): ")
    # ensure input in a valid action:
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
    transcription(PC.PlayerType + ": " + PCAction + "\n" + NPC.PlayerType + ": " + NPCAction + "\n\n") # adds actions to transcript
    # if PC chose attack and NPC also chose attack:
    if PCAction == "Attack" and NPCAction == "Attack": 
        NPCAttack = NPC.Attack() # NPC attack through the class method
        PCAttack = PC.Attack() # PC attack through the class method
        PC.Health -= NPCAttack # PC health is PC health minus NPC attack
        NPC.Health -= PCAttack # NPC health is NPC health minus PC attack
        PCDamage = NPCAttack # PC damage is NPC attack
        NPCDamage = PCAttack # NPC damage is PC attack
    # if PC chose attack and NPC chose dodge:
    elif PCAction == "Attack" and NPCAction == "Dodge": 
        PCAttack = (PC.Attack() - NPC.Dodge()) # PC attack through Character class methods
        NPC.Health -= PCAttack # NPC health is previous health minus the PC attack
        PCDamage = 0 # PC damage is none
        NPCDamage = PCAttack # NPC damage is PC attack through the class methods
    # if PC chose dodge and NPC chose attack:
    elif PCAction == "Dodge" and NPCAction == "Attack":
        NPCAttack = (NPC.Attack() - PC.Dodge()) # NPC attack through Character class methods
        PC.Health -= NPCAttack # PC health is previous health minus the NPC attack
        NPCDamage = 0 # NPC damage is none
        PCDamage = NPCAttack # PC damage is NPC attack through the class methods
    # if PC chose dodge and NPC also chose dodge:
    elif PCAction == "Dodge" and NPCAction == "Dodge":
        PCDamage = 0 # PC damage is none
        NPCDamage = 0 # NPC damage is none
    # ensures doesn't display negetive health values
    if PC.Health < 0:
        PC.Health = 0
    if NPC.Health < 0:
        NPC.Health = 0
    # print results of the round
    PrintResults(PC.PlayerType, NPC.PlayerType, PCDamage, NPCDamage, PC.Health, NPC.Health, NPC.AttackMod, NPC.AttackDice, PC.AttackMod, PC.AttackDice) # inputs variables to function
    # iterate round number
    RoundNum += 1
print("---------- GAME OVER! ---------")
transcription("\n---------- Result ----------\n") # adds to transcript
if NPC.Health <= 0 and PC.Health <= 0: # if both are under or equal to 0 health
    print("You tied. Both characters ended with 0 health.") # prints tied game
    transcription("Game Tied") # adds result to transcript
    print("Thank you for playing, " + PlayerName + ", we hope you'll play again soon!")
elif PC.Health <= 0: # if PC health is under or equal to 0
    print("You lost. Your opponent", NPC.PlayerType, "finished with", NPC.Health, "health.") # prints player lost the game
    transcription(NPC.PlayerType + " (NPC) won") # adds result to transcript
    print("Better luck next time, " + PlayerName + ", we hope you'll play again soon!")
elif NPC.Health <= 0: # if NPC health is under or equal to 0
    print("You Won! Your character", PC.PlayerType, "finished with", PC.Health, "health.") # prints player won the game!
    transcription(PC.PlayerType + " (PC) won") # adds result to transcript
    print("Thank you for playing, " + PlayerName + ", we hope you'll play again soon!")
print("To view the transcript of your game, open the new " + filename + ".csv file on your computer.")