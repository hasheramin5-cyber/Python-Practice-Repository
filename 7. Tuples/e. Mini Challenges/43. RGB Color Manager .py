# A Program to store RGB Colors using Tuples.

colors = (
    ("Red", (255, 0, 0)),
    ("Green", (0, 255, 0)),
    ("Blue", (0, 0, 255))
)

for color, rgb in colors:
    print(f"{color}: {rgb}")

# Explanation:
# The program stores color names along with their RGB values. Each RGB value is itself a tuple containing three numbers representing the intensity of red, green, and blue. The outer loop unpacks each record into the variables 'color' and 'rgb'. Since RGB values never change for a particular color, tuples are an ideal choice for storing them.