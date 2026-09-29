# A Program to acquire a lock with a timeout

import threading
import time


lock = threading.Lock()


def worker_one():
    with lock:
        print("Worker 1 acquired the lock.")

        time.sleep(2)

        print("Worker 1 released the lock.")


def worker_two():
    time.sleep(0.2)

    acquired = lock.acquire(timeout=1)

    if acquired:
        try:
            print("Worker 2 acquired the lock.")

        finally:
            lock.release()

    else:
        print("Worker 2 could not acquire the lock in time.")


thread_one = threading.Thread(target=worker_one)
thread_two = threading.Thread(target=worker_two)


thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()


print("Program finished.")


# Explanation:
# lock.acquire() normally waits until the lock becomes available.
# The timeout parameter limits how long a thread is willing to wait for the lock.
# Worker 1 holds the lock for two seconds.
# Worker 2 attempts to acquire it but only waits for one second.
# If the lock is still unavailable after the timeout, acquire() returns False.
# This allows a program to handle unavailable resources instead of potentially waiting forever.

# Real-Life Use:
# Lock timeouts are useful in systems where waiting forever could cause delays, blocked workers, or resource starvation.