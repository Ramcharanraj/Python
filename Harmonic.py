"""
*Author - Ram Chadran
*Date 18-12-2021
*Time - 10 AM
*Title - Harmonic Number 

"""

def harmonic(num):
    if num <= 0:
        print("Enter the number greater than zero")
        return
    i = 1
    total = 0
    while i <= num:
        print(f"1/{i}")
        total +=1 / i
        i += 1
        print(f"harmonic number is {total}")
        harmonic(int(input("enter the number to find harmonic :")))