# A Program to share a counter between multiple threads

import threading


counter = 0


def increment_counter():
    global counter

    for _ in range(100_000):
        counter += 1


thread_one = threading.Thread(target=increment_counter)
thread_two = threading.Thread(target=increment_counter)


thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()


print("Final counter:", counter)


# Explanation:
# The counter variable is shared by both worker threads.
# Each thread runs increment_counter() and attempts to increase the same counter many times.
# global allows the function to modify the counter defined outside the function.
# Both threads are started before the main thread waits for them using join().
# This example introduces shared mutable data, which becomes important when multiple threads access the same resource.

# Real-Life Use:
# Shared counters can represent statistics, task counts, processed records, or application metrics in concurrent programs.