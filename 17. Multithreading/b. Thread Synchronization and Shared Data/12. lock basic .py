# A Program to protect shared data using a basic lock

import threading


counter = 0

lock = threading.Lock()


def increment_counter():
    global counter

    for _ in range(100_000):
        with lock:
            counter += 1


thread_one = threading.Thread(target=increment_counter)
thread_two = threading.Thread(target=increment_counter)


thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()


print("Final counter:", counter)


# Explanation:
# Lock is a synchronization mechanism that allows only one thread at a time to enter a protected section of code.
# threading.Lock() creates the lock object.
# The with lock statement acquires the lock before modifying the shared counter.
# After the protected code finishes, Python automatically releases the lock.
# This prevents multiple threads from modifying the shared resource at the same time.

# Real-Life Use:
# Locks are useful when multiple threads need to safely modify shared variables, files, collections, or resources.