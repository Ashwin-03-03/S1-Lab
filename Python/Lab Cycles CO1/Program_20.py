str = input("Enter a string: ")

def characterFrequency(str):
    frequency = {}
    for char in str:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    return frequency

print(characterFrequency(str))
        