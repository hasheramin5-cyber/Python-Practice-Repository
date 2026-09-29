# A Program to wait for a thread using join()

import threading
import time


def process_data():
    print("Processing data...")

    time.sleep(2)

    print("Data processing completed.")


thread = threading.Thread(target=process_data)

thread.start()

print("Waiting for the thread...")

thread.join()

print("Main program continues after thread completion.")


# Explanation:
# join() is used when the main thread needs to wait for another thread to finish.
# The process_data() function simulates a time-consuming task.
# start() begins the worker thread.
# The main thread reaches join() and waits while the worker completes its operation.
# Once process_data() finishes, join() returns and the main program continues.

# Real-Life Use:
# join() is useful when later code depends on work completed by a background thread.