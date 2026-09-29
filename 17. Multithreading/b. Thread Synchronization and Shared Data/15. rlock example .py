# A Program to use a reentrant lock with nested function calls

import threading


lock = threading.RLock()


def inner_operation():
    with lock:
        print("Inner operation running.")


def outer_operation():
    with lock:
        print("Outer operation running.")

        inner_operation()


thread = threading.Thread(target=outer_operation)

thread.start()

thread.join()

print("Operation completed.")


# Explanation:
# RLock stands for reentrant lock.
# Unlike a basic Lock, the same thread can acquire an RLock multiple times without blocking itself.
# outer_operation() first acquires the lock.
# It then calls inner_operation(), which tries to acquire the same lock again from the same thread.
# RLock allows this nested acquisition.
# The lock is released as the nested with blocks complete.

# Real-Life Use:
# RLock is useful when related methods may call each other while protecting the same shared resource.