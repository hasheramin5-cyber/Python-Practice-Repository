# A Program to cache function results using a decorator

from functools import wraps


def cache(function):
    stored_results = {}

    @wraps(function)
    def wrapper(number):
        if number in stored_results:
            print("Using cached result.")

            return stored_results[number]

        print("Calculating result...")

        result = function(number)

        stored_results[number] = result

        return result

    return wrapper


@cache
def square(number):
    return number ** 2


print(square(8))
print(square(8))
print(square(10))

# Explanation:
# The cache() decorator stores previously calculated results in a dictionary.
# When square() is called, the decorator first checks whether the argument already exists in stored_results.
# If the result exists, the stored value is returned without executing the original function again.
# If the value does not exist, the original function calculates the result and the decorator stores it.
# Future calls with the same argument can therefore reuse the stored result.

# Real-Life Use:
# Caching is useful for expensive calculations, repeated database queries, API responses, and computational tasks.