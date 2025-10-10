# WAP to print the first n multiples of n

n = int(input("Enter the number upto which you want to print its multiplication table: "))
for i in range(1, n+1):
    print(f"{n} x {i} = {n * i}")
    
    