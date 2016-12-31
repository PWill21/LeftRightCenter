# Left Right Center
# Program: lrc.py
# Name: Patrick Will
# Date: 12/30/2016

#--------Imports--------
import random

#-------- Roll Dice --------

for x in range(1,4):
    roll = random.randint(1,6)
    if roll >=1 and roll <=3:
        result = "H"
    elif roll == 4:
        result = "L"
    elif roll == 5:
        result = "R"
    else:
        if roll == 6:
            result = "C"
    print(result)

    
