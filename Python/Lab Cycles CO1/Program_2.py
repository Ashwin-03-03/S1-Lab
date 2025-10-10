# WAP to swap 2 numbers

def swap2numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    temp=num1
    num1=num2
    num2=temp
    print(f"The swapped numbers are: {num1} and {num2}")
    
swap2numbers()