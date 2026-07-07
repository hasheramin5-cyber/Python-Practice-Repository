# A Program to print numbers from 1 to 10 except 7.

for number in range(1, 11):
    if number == 7:
        continue
    print(number)

# Explanation:
# The program prints numbers from 1 to 10 while skipping the number 7. When the current value becomes 7, the continue statement skips the print statement for that iteration and moves directly to the next number. All other numbers are printed normally.