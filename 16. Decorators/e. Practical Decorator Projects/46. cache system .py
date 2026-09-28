# A Program to create a reusable calculation cache

from functools import wraps


def memoize(function):
    cache = {}

    @wraps(function)
    def wrapper(number):
        if number in cache:
            print(f"Cache hit for {number}")

            return cache[number]

        print(f"Calculating value for {number}")

        result = function(number)

        cache[number] = result

        return result

    return wrapper


@memoize
def fibonacci(number):
    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


print("Fibonacci:", fibonacci(10))


# Explanation:
# The memoize() decorator stores previously calculated function results.
# fibonacci() is recursive, meaning it calls itself with smaller values.
# Without caching, many of the same Fibonacci values would be calculated repeatedly.
# The decorator checks the cache before allowing the function to calculate a value.
# Once a result is calculated, it is stored for future calls.
# This reduces unnecessary repeated calculations.

# Real-Life Use:
# Memoization is useful for recursive algorithms, dynamic programming, expensive calculations, and repeated data access.