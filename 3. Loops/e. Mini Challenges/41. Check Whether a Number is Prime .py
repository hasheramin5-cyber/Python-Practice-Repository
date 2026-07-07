# A Program to check whether a number is prime.

number = int(input("Enter a number: "))

is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a Prime Number.")
else:
    print(f"{number} is not a Prime Number.")

# Explanation:
# The program checks whether a number is prime by testing if it is divisible by any number between 2 and one less than itself. If any divisor is found, the number is not prime and the loop stops immediately using the break statement. Otherwise, the number is declared prime after the loop finishes.