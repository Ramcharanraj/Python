"""
*Author - Ram Chadran
*Date 17-12-2021
*Time - 10 AM
*Title - Facterization

"""

f = 0
num = int(input("Enter the number: "))

for i in range(2, num + 1):
    if num%i == 0:
        for j in range(2, int(i/2)):
            if i%j == 0:
                f = 1
                break
        if f == 0:
            print(i)
