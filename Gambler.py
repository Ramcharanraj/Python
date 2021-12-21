"""

Author : K.Ram Chandran
Date : 21-12-2021
Time : 12 AM
Title : Gambler Simulator
"""

import random

stake = 100
goal = 200

win = 0
loose = 0

while (stake > 0 and stake < goal):

    gamble = random.randint(0, 1)
    if gamble == 0:

        stake -= 1
        loose += 1
    else:

        stake += 1
        win += 1

print("number of wins: ", +win)
winPercentage = (win * 100) / (win + loose)
losspercentage = 100 - winPercentage

print("win percentage is: ", +winPercentage)
print("Loss percentage is: ", +losspercentage)
