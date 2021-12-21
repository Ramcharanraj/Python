"""

Date = '19/12/2021'
Author = 'K.Ram Chandran'
Time - 10 AM
Title = ' 2D-Array Program '

"""
def PrintArray(Rows, Columns):
    array1 = []
    print("Enter the entries row wise:")

    
    for i in range(Rows):  
        array2 = []
        for j in range(Columns):  
            array2.append(input())
        array1.append(array2)

    
    for i in range(Rows):
        for j in range(Columns):
            print(array1[i][j], end=" ")
        print()
try:
    PrintArray(3, 3)
except Exception as e:
    print(e)
