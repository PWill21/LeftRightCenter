# Left Right Center
# Program: lrc.py
# Name: Patrick Will
# Date: 12/30/2016

#--------Imports--------
import random

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
        #return result

#-------- End Functions --------

number_of_players = int(input("How many people are playing? "))
total_pot = str((number_of_players * 3))
print("That's a total of $" + total_pot + " for the winner!")        
rollDice(3)
