# A Program to avoid deadlock by using a consistent lock order

import threading


first_lock = threading.Lock()
second_lock = threading.Lock()


def worker_one():
    with first_lock:
        print("Worker 1 acquired first lock.")

        with second_lock:
            print("Worker 1 acquired second lock.")


def worker_two():
    with first_lock:
        print("Worker 2 acquired first lock.")

        with second_lock:
            print("Worker 2 acquired second lock.")


thread_one = threading.Thread(target=worker_one)
thread_two = threading.Thread(target=worker_two)


thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()


print("Both workers completed safely.")


# Explanation:
# One way to reduce the risk of deadlock is to establish a consistent order for acquiring multiple locks.
# Both worker functions acquire first_lock before second_lock.
# Therefore, one thread cannot hold second_lock while waiting for first_lock at the same time that another thread holds first_lock while waiting for second_lock.
# Consistent lock ordering removes the circular waiting pattern demonstrated by the previous example.

# Real-Life Use:
# Lock ordering is useful in applications where several shared resources must be protected simultaneously.