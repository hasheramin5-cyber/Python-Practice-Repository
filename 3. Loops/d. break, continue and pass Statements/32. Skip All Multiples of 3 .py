# A Program to skip all multiples of 3 using the continue statement.

for number in range(1, 21):
    if number % 3 == 0:
        continue
    print(number)

# Explanation:
# The program prints numbers from 1 to 20 while skipping all multiples of 3. Whenever a number is divisible by 3, the continue statement skips the remaining code for that iteration and moves directly to the next number. This allows the loop to continue without printing multiples of 3.