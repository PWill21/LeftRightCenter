# Left Right Center
# Program: lrc.py
# Name: Patrick Will
# Date: 12/30/2016

#--------Imports--------
import random

#-------- Variables --------
player_list = [] # stores name of each player in a list
number_of_players = 0
playerTotal = [] #stores current amount for each player in a list

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

def enterPlayerNames(): #prompts each user to enter their name
    number_of_players = int(input("How many people are playing? "))
    total_pot = str((number_of_players * 3))
    print ("That's a total of $%s for the winner!" % (total_pot))  
    for x in range(1,number_of_players + 1):
        player_list.append(input("Type your name and press Enter: "))
    return player_list

def displayPlayerNames(n):
    print(n)
    return

def assignTotals(t): # adds an ititial amount of 3 to each players current total
    for x in range(1,len(t) + 1):
        playerTotal.append(3)
    print(playerTotal)
    return
#-------- End Functions --------


enterPlayerNames()
displayPlayerNames(player_list)
assignTotals(player_list)
rollDice(3)



