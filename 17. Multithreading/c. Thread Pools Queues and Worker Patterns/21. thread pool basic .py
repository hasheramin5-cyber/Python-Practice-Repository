# A Program to execute tasks using a thread pool

from concurrent.futures import ThreadPoolExecutor
import time


def task(number):
    print(f"Task {number} started.")

    time.sleep(1)

    print(f"Task {number} finished.")

    return number * 2


with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, range(1, 6))


print("Results:", list(results))


# Explanation:
# ThreadPoolExecutor manages a collection of worker threads for us.
# max_workers=3 means the pool can use up to three worker threads at the same time.
# executor.map() submits the task for each value in the provided iterable.
# The thread pool automatically assigns tasks to available workers.
# The with statement ensures that the executor is properly shut down after the work is completed.
# This avoids manually creating and joining every thread.

# Real-Life Use:
# Thread pools are useful for processing many independent I/O-bound tasks such as downloads, requests, and file work.