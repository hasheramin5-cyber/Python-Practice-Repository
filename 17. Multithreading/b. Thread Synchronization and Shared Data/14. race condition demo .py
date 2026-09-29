# A Program to demonstrate a race condition concept

import threading
import time


counter = 0


def increment_counter():
    global counter

    for _ in range(10):
        current_value = counter

        time.sleep(0.001)

        counter = current_value + 1


thread_one = threading.Thread(target=increment_counter)
thread_two = threading.Thread(target=increment_counter)


thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()


print("Expected counter:", 20)
print("Actual counter:", counter)


# Explanation:
# A race condition can occur when multiple threads access shared data and the final result depends on their timing.
# The counter is first read into current_value.
# The short sleep gives another thread an opportunity to read the same old counter value.
# Both threads can therefore calculate their new value from the same previous value.
# One update can overwrite another update.
# This is why the final result may be lower than the expected value.
# Synchronization mechanisms such as Lock can prevent this type of unsafe shared-data access.

# Real-Life Use:
# Understanding race conditions is essential when working with shared state in concurrent applications.