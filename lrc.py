# Left Right Center
# Program: lrc.py
# Name: Patrick Will
# Date: 12/30/2016

#--------Imports--------
import random

#-------- Variables --------
player_list = []

#-------- Functions --------

def rollDice(number): # number is the number of dice the user is allowed to roll
    for x in range(1,number + 1):
        roll = random.randint(1,6)
        if (roll >=1) and (roll <= 3):
            result = "Hold"
        elif roll == 4:
            result = "Left"
        elif roll == 5:
            result = "Right"
        else:
            result = "Center"
        print(result)
    return

def enterPlayerName(): #prompts each user to enter their name
    #player_list = []
    for x in range(1,number_of_players + 1):
        player_list.append(input("Type your name and press Enter: "))
    return player_list

def displayPlayerNames(n):
    print(n)
    return
    
    
#-------- End Functions --------

number_of_players = int(input("How many people are playing? "))
total_pot = str((number_of_players * 3))
print ("That's a total of $%s for the winner!" % (total_pot))      
enterPlayerName()
rollDice(3)
displayPlayerNames(player_list)


