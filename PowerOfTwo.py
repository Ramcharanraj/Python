"""""
*Author - Ram Chadran
*Date 17-12-2021
*Time - 11:00 AM
*Title - Power Of Two

"""""

i = 0
power = 1

p = int(input("Enter the no to calculate its power: "))

while i <= p:
    print(i , " " ,power)
    power = 2 * power
    i = i + 1