# A Program to combine logging and timing behavior in a decorator

from functools import wraps
import time


def log_and_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Starting {function.__name__}...")

        start_time = time.perf_counter()

        result = function(*args, **kwargs)

        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        print(f"Finished {function.__name__}.")
        print(f"Execution time: {elapsed_time:.6f} seconds.")

        return result

    return wrapper


@log_and_time
def calculate_sum():
    total = 0

    for number in range(1_000_000):
        total += number

    return total


result = calculate_sum()

print("Result:", result)

# Explanation:
# The log_and_time() decorator combines two related behaviors:
# logging and execution-time measurement.

# The wrapper first announces that the function has started.
# time.perf_counter() records the starting point.
# The original function then performs its calculation.
# After completion, another timestamp is recorded.
# The difference between the two timestamps represents the approximate execution time.
# Finally, the original function result is returned.

# Real-Life Use:
# Combined decorators are useful for monitoring application performance while also recording when important operations start and finish.