# Sort a dictionary (ascending and descending)

d1 = {1:"cat", 2:"dog", 3:"rabbit", 4:"monkey"}
print("Ascending order: ", dict(sorted(d1.items())))
print("Descending order: ", dict(sorted(d1.items(), reverse=True)))