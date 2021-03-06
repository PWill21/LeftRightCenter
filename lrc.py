# Left Right Center
# Program: lrc.py
# Name: Patrick Will
# Date: 1/6/2016

#--------Imports--------
import random

#-------- Variables --------
player_list = [] # stores name of each player in a list
number_of_players = 0
player_total_amounts = [] #stores current amount for each player in a list
current_player = ""

#-------- Functions --------


def rollDice(number): # number is the number of dice the user is allowed to roll
    x = 1
    current_player = player_list[x-1]
    print(str(player_list[x-1]) +" rolls:")
    for x in range(1,number + 1):
        roll = random.randint(1,6)
        if (roll >=1) and (roll <= 3):
            result = "Hold"
        elif roll == 4:
            result = "Left"
            #player_total_amounts[x] += 1 # this adds 1 to the amount of the player to the left of the current player
        elif roll == 5:
            result = "Right"
            #player_total_amounts[x+1] += 1 # this add 1 to the amount of the player to the right of the current player
        else:
            result = "Center"
            #player_total_amounts[x-1] -= 1
            # placeholder to add 1 to the current pot
        print(result)
    print(player_total_amounts)
    return

def enterPlayerNames(): #prompts each user to enter their name
    number_of_players = int(input("How many people are playing? "))
    total_pot = str((number_of_players * 3))
    print ("That's a total of $%s for the winner!" % (total_pot))  
    for x in range(1,number_of_players + 1):
        player_list.append(input("Type your name and press Enter: "))
    return player_list

def displayPlayerNames(n): # n is the list of player name returned from the enterPlayerNames() function
    print(n)
    return

def assignTotals(t): # adds an ititial amount of 3 to each players current total
    for x in range(1,len(t) + 1):
        player_total_amounts.append(3)
    #print(player_total_amounts)
    return player_total_amounts
#-------- End Functions --------


enterPlayerNames()
displayPlayerNames(player_list)
assignTotals(player_list)
rollDice(3)



