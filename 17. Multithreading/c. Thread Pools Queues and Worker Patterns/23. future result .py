# A Program to retrieve a result from a Future object

from concurrent.futures import ThreadPoolExecutor
import time


def download_data():
    print("Downloading data...")

    time.sleep(2)

    return "Data downloaded successfully."


with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(download_data)

    print("Task submitted.")

    result = future.result()

    print("Result:", result)


# Explanation:
# submit() returns a Future object immediately after scheduling the task.
# The Future represents the eventual result of the operation.
# The main thread can perform other work before calling result().
# Calling future.result() waits until the worker finishes.
# Once the task completes, result() returns the value returned by the original function.

# Real-Life Use:
# Futures are useful when an application needs to start background work and retrieve its result later.