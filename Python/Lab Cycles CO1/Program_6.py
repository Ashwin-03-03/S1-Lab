# Print the factorial of n where n is input by user

n = int(input("Enter the number which you have to find the factorial: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
    
print(fact)
