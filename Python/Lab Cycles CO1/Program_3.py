# WAP to find the largest of 3 numbers

a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
c = int(input("Enter num3: "))

if(a > b and c):
    print(f"{a} is the largest")
elif(b > a and c):
    print(f"{b} is the largest")
else:
    print(f"{c} is largest")
    

    
