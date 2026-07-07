# A Program to count the number of digits in an integer.

number = abs(int(input("Enter an integer: ")))

count = 0

while number > 0:
    number //= 10
    count += 1

print("Number of Digits =", count)

# Explanation:
# The program counts the total number of digits in an integer using a while loop. It repeatedly removes the last digit of the number by performing floor division by 10 and increases the counter by 1 after each iteration. The loop continues until no digits remain, and the final count is displayed.