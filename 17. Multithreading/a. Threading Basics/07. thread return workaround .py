# A Program to collect a result from a thread using a shared container

import threading


def calculate_square(number, results):
    results.append(number ** 2)


results = []

thread = threading.Thread(
    target=calculate_square,
    args=(8, results)
)


thread.start()

thread.join()

print("Square:", results[0])


# Explanation:
# The target function of a Thread does not directly return its result to the code that called start().
# A simple approach is to provide a shared mutable container such as a list to the worker function.
# calculate_square() calculates the square and stores the result inside the results list.
# join() ensures that the thread has finished before the main thread reads the result.
# After join() returns, results contains the calculated value.

# Real-Life Use:
# Shared containers can be used for simple result collection when worker threads need to provide information back to the main thread.