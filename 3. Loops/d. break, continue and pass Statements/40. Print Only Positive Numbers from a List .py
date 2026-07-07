# A Program to print only positive numbers from a list.

numbers = [-12, 15, -8, 24, 0, -5, 42, 18]

print(f"\n{numbers}")
print("\nOnly Positive Numbers: ")

for number in numbers:
    if number <= 0:
        continue
    print(number)

# Explanation:
# The program prints only the positive numbers from a list. It checks each element one by one, and whenever a number is zero or negative, the continue statement skips that iteration. As a result, only positive numbers are displayed.