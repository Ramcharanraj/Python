"""""
*Author - Ram Chandarn
*Date 17-12-2021
*Time - 10:00 AM
*Title - Flip Coin

"""""

import random
tailCount = 0
headCount = 0
coinResult = 0

count = int(input("Enter Number of Tosses : "))
class FlipCoin:
    for i in range(1,count):
        coinResult = random.uniform(0,1)
        print(coinResult)
        if coinResult < 0.5:
            tailCount += 1
        else:
            headCount += 1
            headPercentage = (headCount / count)*100
            print("Head Percentage is:",headPercentage)
            tailPercentage = (tailCount / count)*100
            print("Tail Percentage is:",tailPercentage)