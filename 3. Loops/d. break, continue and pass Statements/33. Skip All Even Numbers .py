# A Program to print only odd numbers by skipping all even numbers.

for number in range(1, 21):
    if number % 2 == 0:
        continue
    print(number)

# Explanation:
# The program prints only odd numbers between 1 and 20. It checks each number to determine whether it is even. If the number is even, the continue statement skips that iteration. Otherwise, the odd number is printed.