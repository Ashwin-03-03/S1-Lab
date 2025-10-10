# Find the roots of a quadratic equation.
import math

def rootsOfQuadratic():
    a=int(input("Enter the coefficient of x²: "))
    b=int(input("Enter the coefficient of x: "))
    c=int(input("Enter the constant term: "))
    
    d = b*b-4*a*c
    if(d<0):
        print("The roots are not real")
    elif (d>0 or d==0):
        root1=(-b+math.sqrt(d))/2*a
        root2=(-b-math.sqrt(d))/2*a
        print(f"The roots are: {root1} and {root2}")
        
rootsOfQuadratic()
    
