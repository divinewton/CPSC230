-----------------------------------------------
Divi Newton
December 13, 2023
Project Part 4 - Final Project
----------------------------------------------------

README
----------------------------------------------------
This script contains a D&D game in which the user chooses a character (PC) and plays against the computer (NPC) until one of them has no health left and the game is over.
The script uses a while loop to contain the game, iterating every round. The user is asked to choose to either attack or dodge each round. The NPC uses the random library to decide whether to attack or dodge. 
The results are calculated each round based on PC and NPC health, attack rolls, and armor classes.
A transcript of the game is saved to a .csv file to be viewed later.  

Playing the game:
The user is first welcomed and asked to name the transcript file. 
The user is then asked to choose a character. Each character has different stats.
The health indicates how long the character will last in the game. Attack minimum is the minimum health they will take when attacking. Attack dice is the size of their dice for choosing attack. Armor Class is the minimum amount the opponent must roll to hit them. Special attack is a unique attack motifier that can only be used every cooldown cycle.
A larger starting health, larger attack minimum, larger dice, and bigger armor class are what a user should look for in a good character.
The user is asked if they would like to choose the NPC or if it should be assigned randomely. If they choose to choose, they are given the choices and their stats.
Once PC and NPC players are assigned, the game begins. 
In each round, the user must choose to either normal attack, special attack, or dodge. If the user attacks (normal or special), the NPC will loose health. If the NPC attacks, the user looses health. 
The NPC will randomely choose to normal attack, special attack, or dodge each round. 
Whoever's health gets to 0 first looses the game.

The code:
Each character (PC or NPC) is created from inputing values into the Character class to create a new character.
When the user chooses a character, the PC variable is assigned to that character's stats. The same happens when the NPC is assigned. 
Each round, after the user chooses an action, the NPC is assigned a random action through the random library and an if statement. 
The round's outcome is then calculated using the dice roll function and the attack and special result function which are located within the Character class.
The round's results are saved to the transcript using the transcription and print transcript functions, and are also printed in the terminal using the PrintResults function.
At the end of the game, an if statement prints the results based on which character's health is below 0.
Neither player will ever display a health below 0 throughout the game.
The transcript file is accessable on the user's computer to view at any time after the game is completed.