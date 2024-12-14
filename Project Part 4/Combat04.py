# -----------------------------------------------
# Divi Newton
# December 13, 2023
# Project Part 4 - Final Project
# ----------------------------------------------------

import random # imports ramdom library
print("\nWelcome to the combat game!") # welcome to the game
# begin transcript
filename = input("What would you like the game transcript file to be named? ")
transcript = open(filename + ".csv", "w")
transcript.write("---------- Combat Game Transcript ----------\n\n")
transcript.close()
# transcript functions defined:
def transcription(textinput):
    transcript = open(filename + ".csv", "a")
    transcript.write(textinput)
    transcript.close()
def PrintTran(textinput):
    print(textinput)
    transcript = open(filename + ".csv", "a")
    transcript.write(textinput + "\n")
    transcript.close()
# defining the dice rolling function
def DiceRoll(integer):
    result = random.randint(1, integer) # random number between 1 and the input
    return result
# defining character class
class CharacterOption():
    def __init__(self, PlayerType, Health, AttackMod, AttackDice, AC, SpecialAttack, Cooldown, CooldownCount):
        self.PlayerType = PlayerType
        self.Health = Health
        self.AttackMod = AttackMod
        self.AttackDice = AttackDice
        self.AC = AC
        self.SpecialAttack = SpecialAttack
        self.Cooldown = Cooldown
        self.CooldownCount = CooldownCount
    def Attack(self): # defines attack outcomes function
        RollResult = DiceRoll(self.AttackDice) # the dice roll based on the character's attack dice
        Damage = RollResult + self.AttackMod # added the attack mod to dice result
        return Damage
    def SpecialResult(self): # defines special attack outcomes function
        RollResult = DiceRoll(self.AttackDice) # the dice roll based on the character's attack dice
        Damage = RollResult + self.SpecialAttack # added the special attack mod to dice result
        return Damage
    def AttackHit(self, OppAC): # defines function for if attack hits or misses
        RollDice = DiceRoll(20) # rolls a 20-sided dice
        if RollDice > OppAC:
            return "Hit" # return as a hit
        elif RollDice <= OppAC:
            return "Miss" # returns as a miss
# creating 5 PC characters and 3 NPC characters:
PC1 = CharacterOption("Dog", 100, 35, 10, 8, 50, 5, 5)
PC2 = CharacterOption("Cat", 150, 20, 8, 6, 35, 3, 3)
PC3 = CharacterOption("Fish", 70, 10, 5, 3, 25, 2, 2)
PC4 = CharacterOption("Pig", 100, 25, 6, 4, 40, 3, 3)
PC5 = CharacterOption("Goat", 80, 20, 6, 8, 35, 4, 4)
NPC1 = CharacterOption("Bird", 75, 10, 8, 10, 20, 2, 2)
NPC2 = CharacterOption("Raccoon", 100, 30, 10, 12, 45, 5, 5)
NPC3 = CharacterOption("Panther", 200, 40, 14, 16, 55, 6, 6)
# name assignment:
PlayerName = input("Enter your name: ")
PlayerName = PlayerName.strip().title()
transcription("User Name: " + PlayerName + "\n")
# assigning character:
print("\nWelcome " + PlayerName + "! Choose a player to begin!")
print("Your character options are: ") # character options for PC
print(PC1.PlayerType + " (Health: " + str(PC1.Health) + ", Minimum Attack: " + str(PC1.AttackMod) + ", Attack Dice: " + str(PC1.AttackDice) + ", Armor Class: " + str(PC1.AC) + ", Special Attack: " + str(PC1.SpecialAttack) + ", Cooldown: " + str(PC1.Cooldown) + ")")
print(PC2.PlayerType + " (Health: " + str(PC2.Health) + ", Minimum Attack: " + str(PC2.AttackMod) + ", Attack Dice: " + str(PC2.AttackDice) + ", Armor Class: " + str(PC2.AC) + ", Special Attack: " + str(PC2.SpecialAttack) + ", Cooldown: " + str(PC2.Cooldown) + ")")
print(PC3.PlayerType + " (Health: " + str(PC3.Health) + ", Minimum Attack: " + str(PC3.AttackMod) + ", Attack Dice: " + str(PC3.AttackDice) + ", Armor Class: " + str(PC3.AC) + ", Special Attack: " + str(PC3.SpecialAttack) + ", Cooldown: " + str(PC3.Cooldown) + ")")
print(PC4.PlayerType + " (Health: " + str(PC4.Health) + ", Minimum Attack: " + str(PC4.AttackMod) + ", Attack Dice: " + str(PC4.AttackDice) + ", Armor Class: " + str(PC4.AC) + ", Special Attack: " + str(PC4.SpecialAttack) + ", Cooldown: " + str(PC4.Cooldown) + ")")
print(PC5.PlayerType + " (Health: " + str(PC5.Health) + ", Minimum Attack: " + str(PC5.AttackMod) + ", Attack Dice: " + str(PC5.AttackDice) + ", Armor Class: " + str(PC5.AC) + ", Special Attack: " + str(PC5.SpecialAttack) + ", Cooldown: " + str(PC5.Cooldown) + ")")
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
print("\nNow it's time to choose an opponent!\nWould you like to choose the opponent yourself or let the computer decide?")
NPCChoice = input("Enter \"choose\" if you would like to choose, or \"random\" if you would like the computer to choose for you: ")
NPCChoice = NPCChoice.strip()
isChoosing = True
while isChoosing:
    if NPCChoice.lower() == "choose": # if the user chooses to choose their opponent
        print("\nYour opponent options are:") # opponent options
        print(NPC1.PlayerType + " (Health: " + str(NPC1.Health) + ", Minimum Attack: " + str(NPC1.AttackMod) + ", Attack Dice: " + str(NPC1.AttackDice) + ", Armor Class: " + str(NPC1.AC) + ", Special Attack: " + str(NPC1.SpecialAttack) + ", Cooldown: " + str(NPC1.Cooldown) + ")")
        print(NPC2.PlayerType + " (Health: " + str(NPC2.Health) + ", Minimum Attack: " + str(NPC2.AttackMod) + ", Attack Dice: " + str(NPC2.AttackDice) + ", Armor Class: " + str(NPC2.AC) + ", Special Attack: " + str(NPC2.SpecialAttack) + ", Cooldown: " + str(NPC2.Cooldown) + ")")
        print(NPC3.PlayerType + " (Health: " + str(NPC3.Health) + ", Minimum Attack: " + str(NPC3.AttackMod) + ", Attack Dice: " + str(NPC3.AttackDice) + ", Armor Class: " + str(NPC3.AC) + ", Special Attack: " + str(NPC3.SpecialAttack) + ", Cooldown: " + str(NPC3.Cooldown) + ")")
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
print("\nYou chose", PC.PlayerType, "with", PC.Health, "starting health as your player. You will be playing against", NPC.PlayerType, "with", NPC.Health, "starting health.") # prints the chosen player and NPC with health stats
transcription(PC.PlayerType + " (PC) vs. " + NPC.PlayerType + " (NPC)\n")
# defines Print Results function:
def PrintResults(PC, NPC, PCAction, NPCAction, PCRoll, NPCRoll, PCDamage, NPCDamage, PCHealth, NPCHealth, PCAttackMod, NPCAttackMod, PCAttackDice, NPCAttackDice, PCSpecialAttack, NPCSpecialAttack, PCHit, NPCHit): # takes in variables
    if PCRoll and NPCRoll >= 1:
        if PCHit == True and NPCHit == True: # if both hit their opponent
            PrintTran("\n" + PC + " (PC) chose to " + PCAction + " and rolled a " + str(PCRoll) + ". " + PC + " hit " + NPC + " with " + str(NPCDamage) + " damage.") # prints PC stats
            PrintTran(NPC + " (NPC) chose to " + NPCAction + " and rolled a " + str(NPCRoll) + ". " + NPC + " hit " + PC + " with " + str(PCDamage) + " damage.") # prints NPC stats
            PrintTran(PC + " has " + str(PCHealth) + " remaining health.")
            PrintTran(NPC + " has " + str(NPCHealth) + " remaining health.")
        elif PCHit == True and NPCHit == False: # if PC hits their opponent
            PrintTran("\n" + PC + " (PC) chose to " + PCAction + " and rolled a " + str(PCRoll) + ". " + PC + " hit " + NPC + " with " + str(NPCDamage) + " damage.") # prints PC stats
            PrintTran(NPC + " (NPC) chose to " + NPCAction + " and rolled a " + str(NPCRoll) + ". " + NPC + " did not hit " + PC + ".") # prints NPC stats
            PrintTran(PC + " has " + str(PCHealth) + " remaining health.")
            PrintTran(NPC + " has " + str(NPCHealth) + " remaining health.")
        elif PCHit == False and NPCHit == True: # if NPC hit their opponent
            PrintTran("\n" + PC + " (PC) chose to " + PCAction + " and rolled a " + str(PCRoll) + ". " + PC + " did not hit " + NPC + ".") # prints PC stats
            PrintTran(NPC + " (NPC) chose to " + NPCAction + " and rolled a " + str(NPCRoll) + ". " + NPC + " hit " + PC + " with " + str(PCDamage) + " damage.") # prints NPC stats
            PrintTran(PC + " has " + str(PCHealth) + " remaining health.")
            PrintTran(NPC + " has " + str(NPCHealth) + " remaining health.")
        elif PCHit == False and NPCHit == False: # if neither hit their opponent
            PrintTran("\n" + PC + " (PC) chose to " + PCAction + " and rolled a " + str(PCRoll) + ". " + PC + " did not hit " + NPC + ".") # prints NPC stats
            PrintTran(NPC + " (NPC) chose to " + NPCAction + " and rolled a " + str(NPCRoll) + ". " + NPC + " did not hit " + PC + ".") # prints NPC stats
            PrintTran(PC + " has " + str(PCHealth) + " remaining health.")
            PrintTran(NPC + " has " + str(NPCHealth) + " remaining health.")
        if PCDamage == NPCAttackMod + NPCAttackDice or PCDamage == NPCAttackDice + NPCSpecialAttack:
            PrintTran("-- NPC rolled max damage! --")
        if NPCDamage == PCAttackMod + PCAttackDice or NPCDamage == PCAttackDice + PCSpecialAttack:
            PrintTran("-- PC rolled max damage! --")
        if PCDamage == NPCAttackMod + 1 or PCDamage == NPCSpecialAttack + 1:
            PrintTran("-- NPC rolled minimum damage --")
        if NPCDamage == PCAttackMod + 1 or PCDamage == PCSpecialAttack + 1:
            PrintTran("-- PC rolled minimum damage --")
    elif PCRoll == 0 or NPCRoll == 0:
        if PCRoll == 0 and NPCRoll == 0:
            PrintTran("\n" + PC + " (PC) and " + NPC + " both chose to Dodge and both players did not roll.") # prints ending stats
            PrintTran(PC + " has " + str(PCHealth) + " remaining health.")
            PrintTran(NPC + " has " + str(NPCHealth) + " remaining health.")
        elif PCRoll == 0 and NPCRoll != 0:
            PrintTran("\n" + PC + " (NPC) chose to " + PCAction + " and both players did not roll.") # prints ending stats
            PrintTran(PC + " has " + str(PCHealth) + " remaining health.")
            PrintTran(NPC + " has " + str(NPCHealth) + " remaining health.")
        elif NPCRoll == 0 and PCRoll !=0:
            PrintTran("\n" + NPC + " (NPC) chose to " + NPCAction + " and both players did not roll.") # prints ending stats
            PrintTran(PC + " has " + str(PCHealth) + " remaining health.")
            PrintTran(NPC + " has " + str(NPCHealth) + " remaining health.")
# starting the game: 
print("Let's get started, " + PlayerName + "!\n")
RoundNum = 1 # sets round number of the game
# playing the game:
while PC.Health > 0 and NPC.Health > 0: # ensured both players still hahe health
    print("\n---------- ROUND", RoundNum, "---------\n")
    transcription("\n---------- Round #" + str(RoundNum) + " ----------\n") # adds round to transcript
    PCAction = input("Choose your action (Normal Attack, Special Attack or Dodge): ")
    # ensure input in a valid action:
    PCAction = PCAction.strip()
    while True: 
        if PCAction.lower() == "normal attack" or PCAction.lower() == "special attack" or PCAction.lower() == "dodge":
            break
        else:
            print("You entered an incorrect action.") # ensured action was entered correctly
            PCAction = input("Please choose \"Normal Attack\", \"Special Attack\" or \"Dodge\" to continue: ")
            PCAction = PCAction.strip()
    # ensures if special action, PC is past cooldown period
    if PCAction == "special attack":
        if PC.CooldownCount >= PC.Cooldown:
            PCAction = "special attack"
            PC.CooldownCount = 0 # sets cooldown count back at 0
        elif PC.CooldownCount < PC.Cooldown:
            PCAction = "normal attack"
            print("You have not reached your cooldown time, action has been adjusted to \"Normal Attack\"")
    PCAction = PCAction.title()
    # assigns NPC with a random action:
    RandNum = random.randint(0, 2) # chooses random number (either 0, 1, or 2)
    if RandNum == 0:
        NPCAction = "Normal Attack" # if the number is 0, NPC norlam attacks
    elif RandNum == 1:
        NPCAction = "Special Attack" # if the number is 1, NPC special attacks
    elif RandNum == 2:
        NPCAction = "Dodge" # if the number is 2, NPC dodges
     # ensures if special action, NPC is past cooldown period
    if NPCAction == "Special Attack":
        if NPC.CooldownCount >= NPC.Cooldown:
            NPCAction = "Special Attack"
            NPC.CooldownCount = 0 # sets cooldown count back at 0
        elif NPC.CooldownCount < NPC.Cooldown:
            NPCAction = "Normal Attack"
    # outcome of the round:
    transcription(PC.PlayerType + ": " + PCAction + "\n" + NPC.PlayerType + ": " + NPCAction + "\n") # adds actions to transcript
    # if PC and NPC both choose normal attack or special attack:
    if (PCAction == "Normal Attack" or PCAction == "Special Attack") and (NPCAction == "Normal Attack" or NPCAction == "Special Attack"):
        # sets attack variables to correct class methods
        if PCAction == "Special Attack":
            PCAttack = PC.SpecialResult() # PC attack through the special result class method
            PCRoll = PCAttack - PC.SpecialAttack # assigns roll result
        elif PCAction == "Normal Attack":
            PCAttack = PC.Attack() # PC attack through the attack class method
            PCRoll = PCAttack - PC.AttackMod # assigns roll result
            PC.CooldownCount += 1 # adds 1 to cooldown count
        if NPCAction == "Special Attack":
            NPCAttack = NPC.SpecialResult() # NPC attack through the special result class method
            NPCRoll = NPCAttack - NPC.SpecialAttack # assigns roll result
        elif NPCAction == "Normal Attack":
            NPCAttack = NPC.Attack() # NPC attack through the attack class method
            NPCRoll = NPCAttack - NPC.AttackMod # assigns roll result
            NPC.CooldownCount += 1 # adds 1 to cooldown count
        # changes results if attack hit or missed
        if NPC.AttackHit(PC.AC) == "Hit":
            NPCHit = True
            PC.Health -= NPCAttack # PC health is PC health minus NPC attack
            PCDamage = NPCAttack # PC damage is NPC attack
        else:
            NPCHit = False
            PC.Health = PC.Health
            PCDamage = 0
        if PC.AttackHit(NPC.AC) == "Hit":
            PCHit = True
            NPC.Health -= PCAttack # NPC health is NPC health minus PC attack
            NPCDamage = PCAttack # NPC damage is PC attack
        else:
            PCHit = False
            NPC.Health = NPC.Health
            NPCDamage = 0
    # if either PC or NPC chooses dodge:
    elif PCAction == "Dodge" or NPCAction == "Dodge":
        if PCAction == "Dodge" and NPCAction == "Dodge":
            PCRoll = 0 # sets to 0 because did not roll
            NPCRoll = 0 # sets to 0 because did not roll
        elif PCAction == "Dodge":
            PCRoll = 0 # sets to 0 because did not roll
            NPCRoll = 1 # sets to 1 to differentiate
        elif NPCAction == "Dodge":
            NPCRoll = 0 # sets to 0 because did not roll
            PCRoll = 1 # sets to 1 to differentiate
        PCDamage = 0 # PC damage is none
        NPCDamage = 0 # NPC damage is none
        PC.CooldownCount += 1 # adds 1 to PC cooldown count
        NPC.CooldownCount += 1 # adds 1 to NPC cooldown count
        PCHit = False
        NPCHit = False
    # ensures doesn't display negetive health values
    if PC.Health < 0:
        PC.Health = 0
    if NPC.Health < 0:
        NPC.Health = 0
    # print results of the round
    PrintResults(PC.PlayerType, NPC.PlayerType, PCAction, NPCAction, PCRoll, NPCRoll, PCDamage, NPCDamage, PC.Health, NPC.Health, PC.AttackMod, NPC.AttackMod, PC.AttackDice, NPC.AttackDice, PC.SpecialAttack, NPC.SpecialAttack, PCHit, NPCHit) # inputs variables to function
    # iterate round number
    RoundNum += 1
print("\n---------- GAME OVER! ---------\n")
transcription("\n---------- Result ----------\n") # adds to transcript
if NPC.Health <= 0 and PC.Health <= 0: # if both are under or equal to 0 health
    print("You Won by a hair! Your character", PC.PlayerType, "went first and defeated your opponent before", NPC.PlayerType, "got a change to attack.") # prints player won the game!
    transcription(PC.PlayerType + " (PC) won") # adds result to transcript
    print("Thank you for playing, " + PlayerName + ", we hope you'll play again soon!")
elif PC.Health <= 0: # if PC health is under or equal to 0
    print("You lost. Your opponent", NPC.PlayerType, "finished with", NPC.Health, "health.") # prints player lost the game
    transcription(NPC.PlayerType + " (NPC) won\n" + NPC.PlayerType + " ended with " + str(NPC.Health) + " health.") # adds result to transcript
    print("Better luck next time, " + PlayerName + ", we hope you'll play again soon!")
elif NPC.Health <= 0: # if NPC health is under or equal to 0
    print("You Won! Your character", PC.PlayerType, "finished with", PC.Health, "health.") # prints player won the game!
    transcription(PC.PlayerType + " (PC) won\n" + PC.PlayerType + " ended with " + str(PC.Health) + " health.") # adds result to transcript
    print("Thank you for playing, " + PlayerName + ", we hope you'll play again soon!")
print("\nTo view the transcript of your game, open the new " + filename + ".csv file on your computer.\n") # prints info for accessing transcript