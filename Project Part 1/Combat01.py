# -----------------------------------------------
# Divi Newton
# October 19, 2023
# Project Part 1
# ----------------------------------------------------

# dictionaries containing player and NPC types, health, attack, and dodge modifier numbers:
PC1 = {"PlayerType": "Dog", "Health": 75, "Attack": 15, "Dodge": 0.50}
PC2 = {"PlayerType": "Cat", "Health": 100, "Attack": 10, "Dodge": 0.75}
NPC1 = {"PlayerType": "Bird", "Health": 25, "Attack": 10, "Dodge": 0.20}
NPC2 = {"PlayerType": "Raccoon", "Health": 50, "Attack": 15, "Dodge": 0.50}
NPC3 = {"PlayerType": "Panther", "Health": 75, "Attack": 45, "Dodge": 0.80}
# welcome to the game:
print("Welcome to the combat game!")
PCDiff = input("Choose a game difficulty (Easy, Medium, or Challenging): ")
PCDiff = PCDiff.strip()
# assigns game difficulty:
while True:
    if PCDiff.lower() == "easy": 
        NPC = NPC1 # if user chooses easy, NPC is set to NPC1
        break
    elif PCDiff.lower() == "medium":
        NPC = NPC2 # if user chooses medium, NPC is set to NPC2
        break
    elif PCDiff.lower() == "challenging":
        NPC = NPC3 # if user chooses challenging, NPC is set to NPC3
        break
    else:
        print("You entered an incorrect difficulty.") # if user enters incorrect difficulty, they are asked again
        PCDiff = input("Enter \"Easy,\" \"Medium,\" or \"Challenging\": ")
        PCDiff = PCDiff.strip()
print("You chose", PCDiff.title(), "as the game difficulty!")
# assigning character:
print("Choose a player to begin:")
print("Your character options are", PC1["PlayerType"], "or", PC2["PlayerType"], "!", PC1["PlayerType"], "has", PC1["Health"], "health,", PC1["Attack"], "attack, and", PC1["Dodge"], "dodge.", PC2["PlayerType"], "has", PC2["Health"], "health,", PC2["Attack"], "attack, and", PC2["Dodge"], "dodge.")
Character = input("Please choose \"Dog\" or \"Cat\" to continue: ") # user is asked to enter a player choice after seeing the options
Character = Character.strip()
# ensures correct character entered, assigns character PC variable:
while True: 
    if Character.lower() == "dog" or Character.lower() == "cat":
        if Character.lower() == "dog": # if they enter dog, PC is set to PC1
            PC = PC1
            break
        elif Character.lower() == "cat": # if they enter cat, PC is set to PC2
            PC = PC2
            break
    else:
        print("You entered an incorrect player.") # if entered an incorrect player, prompted again 
        Character = input("Please choose \"Dog\" or \"Cat\" to continue: ")
        Character = Character.strip()
print("You chose", PC["PlayerType"], "with", PC["Health"], "starting health. You will be playing against", NPC["PlayerType"], "with", NPC["Health"], "starting health.") # prints the chosen player and NPC with health stats
# starting the game: 
print("Let's get started!")
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
    import random # imports ramdom library
    RandNum = random.randint(0, 1) # chooses random number (either 0 or 1)
    if RandNum == 1:
        NPCAction = "Attack" # if the number is 1, NPC attacks
    elif RandNum == 0:
        NPCAction = "Dodge" # if the number is 0, NPC dodges
    # outcome of the round:
    print("You chose to", PCAction, "and your opponent chose to", NPCAction) # prints both players action choices
    # if PC chose attack and NPC also chose attack:
    if PCAction == "Attack" and NPCAction == "Attack": 
        PC["Health"] -= NPC["Attack"] # PC health is PC health minus NPC attack
        NPC["Health"] -= PC["Attack"] # NPC health is NPC health minus PC attack
        PCDamage = NPC["Attack"] # PC damage is NPC attack
        NPCDamage = PC["Attack"] # NPC damage is PC attack
    # if PC chose attack and NPC chose dodge:
    elif PCAction == "Attack" and NPCAction == "Dodge": 
        NPC["Health"] -= (PC["Attack"] * NPC["Dodge"]) # NPC health is NPC health minus PC attack times NPC dodge
        PCDamage = 0 # PC damage is none
        NPCDamage = (PC["Attack"] * NPC["Dodge"]) # NPC damage is PC attack times NPC damage
    # if PC chose dodge and NPC chose attack:
    elif PCAction == "Dodge" and NPCAction == "Attack":
        PC["Health"] -= (NPC["Attack"] * PC["Dodge"]) # PC health is PC health minus NPC attack times PC dodge
        PCDamage = (NPC["Attack"] * PC["Dodge"]) # PC damage is NPC attack times PC dodge
        NPCDamage = 0 # NPC damage is none
    # if PC chose dodge and NPC also chose dodge:
    elif PCAction == "Dodge" and NPCAction == "Dodge":
        PCDamage = 0 # PC damage is none
        NPCDamage = 0 # NPC damage is none
    # print results of the round:
    print("Your character,", PC["PlayerType"], "took", PCDamage, "damage, and your opponent", NPC["PlayerType"], "took", NPCDamage, "damage.") # prints round damage
    print("Your current health is", PC["Health"], "and your opponent's health is", NPC["Health"]) # prints current PC and NPC health
    # iterate round number
    RoundNum += 1
print("---------- GAME OVER! ---------")
if NPC["Health"] <= 0 and PC["Health"] <= 0: # if both are under or equal to 0 health
    print("You tied. Both characters ended with 0 health.") # prints tied game
    print("Thank you for playing, we hope you'll play again soon!")
elif PC["Health"] <= 0: # if PC health is under or equal to 0
    print("You lost. Your opponent", NPC["PlayerType"], "finished with", NPC["Health"], "health.") # prints player lost the game
    print("Better luck next time, we hope you'll play again soon!")
elif NPC["Health"] <= 0: # if NPC health is under or equal to 0
    print("You Won! Your character", PC["PlayerType"], "finished with", PC["Health"], "health.") # prints player won the game!
    print("Thank you for playing, we hope you'll play again soon!")