"""""
*Author - Ram Chadran
*Date 17-12-2021
*Time - 12:00 PM
*Title - Power Of Two

"""""



year = int(input("Enter the Year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is leap year")
else:
 print(year,"not a leap year")
