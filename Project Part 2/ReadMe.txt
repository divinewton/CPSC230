-----------------------------------------------
Divi Newton
November 3, 2023
Project Part 2

Collaborators:
Dylan Ravel
----------------------------------------------------

README
----------------------------------------------------
This script contains a D&D game in which the user chooses a character (PC) and plays against the computer (NPC) until one of them has no health left and the game is over.
The script uses a while loop to contain the game, iterating every round. The user is asked to choose to either attack or dodge each round. The NPC uses the random library to decide whether to attack or dodge. 
The results are calculated each round based on PC and NPC health and attack and dodge dice rolls. 

Playing the game:
The user is first welcomed to the game and asked to choose a character. Each character has different stats.
The health indicates how long the character will last in the game. Attack minimum is the minimum health they will take when attacking. Attack dice is the size of their dice for choosing attack. Dodge dice is the size of their dice for choosing dodge.
A larger starting health, larger attack minimum, and larger dice are what a user should look for in a good character.
The user is asked if they would like to choose the NPC or if it should be assigned randomely.
If they choose to choose, they are given the choices and their stats.
Once PC and NPC players are assigned, the game begins. 
In each round, the user must choose to either attack or dodge. If the user attacks, the NPC will loose health. If the NPC attacks, the user looses health. 
The NPC will randomely choose to attack or dodge each round. 
Whoever's health gets to 0 first looses the game.

The code:
Each character (PC or NPC) is in a dictionary with its stats.
When the user chooses a character, the PC variable  is assigned to the dictionary containing their chosen character's stats.
The same happens when the NPC is assigned. 
Each round, after the user chooses an action, the NPC is assigned a random action through the random library and an if statement. 
The round's outcome is then calculated using the dice roll function, damage function, and dodge function, as well as an if statement with an elif for each possible attack or dodge combination. 
At the end of the game, an if statement prints the results based on which character's health is below 0.
Neither player will ever display a health below 0. 