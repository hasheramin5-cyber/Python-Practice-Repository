# A Program to manage multiple Future objects

from concurrent.futures import ThreadPoolExecutor
import time


def process_number(number):
    time.sleep(0.5)

    return number * number


numbers = [2, 4, 6, 8, 10]


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [
        executor.submit(process_number, number)
        for number in numbers
    ]

    results = [
        future.result()
        for future in futures
    ]


print("Numbers:", numbers)
print("Squares:", results)


# Explanation:
# Multiple tasks can be submitted to the same thread pool.
# Each call to submit() returns a separate Future object.
# The futures list stores all of these Future objects.
# Calling result() on each Future retrieves the corresponding completed value.
# The results list follows the same order as the futures list, regardless of the order in which worker threads actually complete their tasks.

# Real-Life Use:
# Multiple futures are useful when many independent tasks need to be launched and their results collected together.