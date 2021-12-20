"""
*Author - Ram Chadran
*Date - 19-12-2021
*Time - 10 AM
*Title - Euclidean Distance

"""

import math
def CalculateDistance(x, y):
    # calculating distance
    distance= math.sqrt(pow(x, 2)+pow(y, 2))

    # print distance
    print(distance)

try:
    #taking inputs x and y
    x=int(input('enter x value: '))
    y=int(input('enter y value: '))
    CalculateDistance(x, y)
except Exception as e:
    print(e)