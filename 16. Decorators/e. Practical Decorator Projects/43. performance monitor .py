# A Program to monitor the performance of a function

from functools import wraps
import time


def performance_monitor(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = function(*args, **kwargs)

        elapsed_time = time.perf_counter() - start_time

        print(
            f"{function.__name__} completed in "
            f"{elapsed_time:.6f} seconds."
        )

        return result

    return wrapper


@performance_monitor
def process_data():
    total = 0

    for number in range(500_000):
        total += number

    return total


result = process_data()

print("Result:", result)


# Explanation:
# The performance_monitor() decorator measures the execution time of the decorated function.
# A starting timestamp is recorded before process_data() begins.
# The function then performs its calculation and returns a result.
# After the function completes, the elapsed time is calculated.
# The measured duration is displayed while the original function result is still returned to the caller.
# This allows performance information to be added without changing the function's internal calculation.

# Real-Life Use:
# Performance monitoring is useful for identifying slow functions, benchmarking code, and optimizing applications.