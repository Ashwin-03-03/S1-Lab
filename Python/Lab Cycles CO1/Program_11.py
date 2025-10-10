# WAP to reverse the first and last characters of a string

def first_last_swap():
    str = input("Enter the string you want to swap: ")
    if(len(str)<2):
        return str
    else:
        return str[-1]+str[1:-1]+str[0]
    
print(first_last_swap())