# A Program to submit individual tasks to a thread pool

from concurrent.futures import ThreadPoolExecutor
import time


def calculate_square(number):
    time.sleep(0.5)

    return number ** 2


with ThreadPoolExecutor(max_workers=3) as executor:
    future_one = executor.submit(calculate_square, 5)
    future_two = executor.submit(calculate_square, 8)
    future_three = executor.submit(calculate_square, 10)

    print("Result 1:", future_one.result())
    print("Result 2:", future_two.result())
    print("Result 3:", future_three.result())


# Explanation:
# executor.submit() schedules one function call for execution by a worker thread.
# Instead of immediately returning the final value, submit() returns a Future object.
# Each Future represents the pending or completed result of one submitted task.
# Calling result() waits for that task to finish and then returns its value.
# This provides more control than executor.map() because individual tasks can be submitted and tracked separately.

# Real-Life Use:
# Individual task submission is useful when different tasks have different arguments or need to be monitored separately.