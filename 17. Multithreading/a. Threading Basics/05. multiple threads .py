# A Program to run multiple threads

import threading
import time


def task(name):
    print(f"{name} started.")

    time.sleep(1)

    print(f"{name} finished.")


thread_one = threading.Thread(
    target=task,
    args=("Task 1",)
)

thread_two = threading.Thread(
    target=task,
    args=("Task 2",)
)

thread_three = threading.Thread(
    target=task,
    args=("Task 3",)
)


thread_one.start()
thread_two.start()
thread_three.start()


thread_one.join()
thread_two.join()
thread_three.join()


print("All tasks completed.")


# Explanation:
# Multiple Thread objects can be created when several independent tasks need to run concurrently.
# Each thread receives the same task() function but a different name through the args parameter.
# Starting all three threads allows them to perform their waiting work concurrently.
# Each join() ensures that the main program waits for the corresponding thread to finish.
# The exact order in which thread output appears can vary because thread scheduling is controlled by the system.

# Real-Life Use:
# Multiple threads can be useful for handling several independent I/O-bound tasks such as downloads or requests.