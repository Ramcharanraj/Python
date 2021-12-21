"""
Author - Ram Chadran
Date - 20-12-2021
Time - 11 AM
Title - SumOfTwo

"""
def findTriplets(array, n):
    try:
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if array[i] + array[j] + array[k] == 0:
                        found = True
                        print(array[i], array[j], array[k])

    except Exception as e:
        print(e)

        
    if found == False:
        print(" not exist ")

array = [0, -1, 2, -3, 1]
n = len(array)
findTriplets(array, n)
