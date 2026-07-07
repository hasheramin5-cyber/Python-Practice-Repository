# A Program to stop printing numbers when the number reaches 5 using the break statement.

for number in range(1, 11):
    if number == 5:
        break
    print(number)

# Explanation:
# The program prints numbers from 1 to 10 using a for loop. When the value of the variable 'number' becomes 5, the break statement immediately terminates the loop. As a result, only the numbers 1 to 4 are printed, demonstrating how the break statement is used to exit a loop before it finishes.