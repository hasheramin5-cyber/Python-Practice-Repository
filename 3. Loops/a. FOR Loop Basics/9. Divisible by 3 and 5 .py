# A Program to Print All Numbers Divisible by Both 3 and 5 Between 1 and 100.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(number)
        