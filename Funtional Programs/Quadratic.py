"""
*Author - Ram Chadran
*Date - 19-12-2021
*Time - 10 AM
*Title - Quadratic 

"""
import cmath
def QuadraticCalculation(a, b, c):
    try:
        # Calculation
        delta= (b*b)-(4*a*c)
        root1=(-b + cmath.sqrt(delta))/(2*a)
        root2=(-b - cmath.sqrt(delta))/(2*a)

        # printing value
        print(root1)
        print(root2)
    except Exception as e:
        print(e)

try:
    # input values
    a=int(input('enter value of a: '))
    b=int(input('enter value of b: '))
    c=int(input('enter value of c: '))
    QuadraticCalculation(a, b, c)
except Exception as e:
    print(e)