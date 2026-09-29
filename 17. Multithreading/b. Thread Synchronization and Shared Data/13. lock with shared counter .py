# A Program to safely update shared data using a lock

import threading


balance = 1000

lock = threading.Lock()


def deposit(amount):
    global balance

    with lock:
        balance += amount

        print(f"Deposited: {amount}")
        print(f"Current balance: {balance}")


thread_one = threading.Thread(
    target=deposit,
    args=(500,)
)

thread_two = threading.Thread(
    target=deposit,
    args=(300,)
)


thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()


print("Final balance:", balance)


# Explanation:
# The balance variable is shared by multiple threads.
# Both threads attempt to modify the same bank balance.
# The lock protects the balance update so that only one thread can execute that section at a time.
# The with statement automatically acquires and releases the lock.
# After both threads finish, the main thread displays the final balance.

# Real-Life Use:
# This pattern is useful for shared financial values, inventory quantities, counters, and other resources where simultaneous updates must be controlled.