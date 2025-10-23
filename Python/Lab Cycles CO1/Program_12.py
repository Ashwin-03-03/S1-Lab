# Display first and last colors from a list of comma-separated color names.

# Create a list of colors
colors = []
while True:
    color = input("Enter the colors you want or type 'done' to finish: ")
    if (color.lower()=="done"):
        break
    else:
        colors.append(color)
print(f"You have entered these colors: {colors}")

first_color = colors[0]
last_color = colors[-1]
print(f"The first color is {first_color} and last color is {last_color}")

