# A Program to preserve a function's return value through a decorator

def double_result(function):
    def wrapper(number):
        result = function(number)

        return result * 2

    return wrapper


@double_result
def calculate(number):
    return number + 5


result = calculate(10)

print("Result:", result)


# Explanation:
# A decorator can modify not only what happens before or after a function but also the value returned by the function.
# calculate() returns number + 5.
# The wrapper() calls calculate() and stores its result.
# The result is then multiplied by 2 before being returned to the caller.
# For input 10, calculate() returns 15.
# The decorator changes the final returned value to 30.

# Real-Life Use:
# Return-value decorators can be useful for transforming, validating, formatting, or processing function results.