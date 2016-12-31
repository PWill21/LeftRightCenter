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
        print(roll)
        #return roll

rollDice(1)
