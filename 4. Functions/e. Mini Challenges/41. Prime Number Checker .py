# A Program to check whether a number is prime using a function.

# Definition:
# A prime number is a natural number greater than 1 that has exactly two factors: 1 and itself.

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

number = int(input("\nEnter a number: "))

if is_prime(number):
    print(f"{number} is a Prime Number.")
else:
    print(f"{number} is not a Prime Number.")

# Explanation:
# The program defines a function that checks whether a number is prime. The function returns True if the number has no divisors other than 1 and itself, otherwise it returns False. The returned value is then used to display whether the entered number is prime.