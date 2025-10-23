# Print the triangular star pattern using nested loops in Python
# n=int(input("Enter the number of rows of triangular star pattern you want to print: "))
n=5
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
    
    

    