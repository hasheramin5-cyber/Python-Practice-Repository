# A Program to demonstrate the concept of a deadlock

import threading


lock_one = threading.Lock()
lock_two = threading.Lock()


def worker_one():
    with lock_one:
        print("Worker 1 acquired lock one.")

        with lock_two:
            print("Worker 1 acquired lock two.")


def worker_two():
    with lock_two:
        print("Worker 2 acquired lock two.")

        with lock_one:
            print("Worker 2 acquired lock one.")


thread_one = threading.Thread(target=worker_one)
thread_two = threading.Thread(target=worker_two)


thread_one.start()
thread_two.start()


thread_one.join(timeout=1)
thread_two.join(timeout=1)


print("Deadlock demonstration finished.")


# Explanation:
# A deadlock can occur when two or more threads wait for resources held by each other.
# Worker 1 acquires lock_one and then attempts to acquire lock_two.
# Worker 2 acquires lock_two and then attempts to acquire lock_one.
# If both threads acquire their first lock before requesting the second one, each thread can wait indefinitely for the other thread to release its lock.
# The timeout on join() prevents the main thread from waiting forever in this demonstration.
# The example is intentionally designed to show the danger of inconsistent lock acquisition order.

# Real-Life Use:
# Understanding deadlocks is important when multiple locks protect shared resources in concurrent applications.