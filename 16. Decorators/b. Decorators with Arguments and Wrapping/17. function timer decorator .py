# A Program to measure function execution time using a decorator

from functools import wraps
import time


def timer(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = function(*args, **kwargs)

        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        print(f"{function.__name__} took {elapsed_time:.6f} seconds.")

        return result

    return wrapper


@timer
def calculate_sum():
    total = 0

    for number in range(1_000_000):
        total += number

    return total


result = calculate_sum()

print("Result:", result)


# Explanation:
# The timer() decorator measures how long a function takes to complete.
# time.perf_counter() provides a high-resolution timer.
# The first call records the starting time.
# The original function then performs its calculation.
# After the function finishes, the ending time is recorded.
# Subtracting the starting time from the ending time gives the approximate execution duration.
# The original result is returned unchanged.

# Real-Life Use:
# Timing decorators are useful for performance testing, optimization, benchmarking, and identifying slow functions.