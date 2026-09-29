# A Program to handle exceptions raised by thread pool tasks

from concurrent.futures import ThreadPoolExecutor


def divide(first, second):
    return first / second


with ThreadPoolExecutor(max_workers=2) as executor:
    successful_task = executor.submit(divide, 20, 4)
    failed_task = executor.submit(divide, 20, 0)

    try:
        print("Successful result:", successful_task.result())

    except Exception as error:
        print("Successful task failed:", error)

    try:
        print("Failed result:", failed_task.result())

    except Exception as error:
        print("Failed task:", error)


# Explanation:
# Exceptions raised inside a ThreadPoolExecutor worker are associated with the corresponding Future.
# The worker thread does not directly crash the main program when the exception occurs.
# Calling result() on the Future re-raises the exception in the thread that requests the result.
# The try-except blocks therefore allow the main program to handle each task's failure independently.
# This is an important part of safely managing background operations.

# Real-Life Use:
# Future exception handling is useful for network requests, file operations, database tasks, and other background jobs that may fail independently.