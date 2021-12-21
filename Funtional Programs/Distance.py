"""
Author - Ram Chadran
Date - 19-12-2021
Time - 10 AM
Title - Euclidean Distance

"""

import math
def CalculateDistance(x, y):
    
    distance= math.sqrt(pow(x, 2)+pow(y, 2))

    
    print(distance)

try:
    
    x=int(input('enter x value: '))
    y=int(input('enter y value: '))
    CalculateDistance(x, y)
except Exception as e:
    print(e)