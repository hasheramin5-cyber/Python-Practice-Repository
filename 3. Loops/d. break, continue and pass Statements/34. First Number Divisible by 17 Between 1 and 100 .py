# A Program to find the first number divisible by 17 between 1 and 100.

for number in range(1, 101):
    if number % 17 == 0:
        print("First Number:", number)
        break

# Explanation:
# The program searches for the first number between 1 and 100 that is divisible by 17. As soon as such a number is found, it is displayed and the break statement immediately terminates the loop. This avoids checking the remaining numbers once the required result has been found.