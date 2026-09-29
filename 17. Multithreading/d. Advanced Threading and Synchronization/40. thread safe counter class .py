# A Program to build a thread-safe counter class

import threading


class SafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1

    def get_value(self):
        with self.lock:
            return self.value


counter = SafeCounter()


def worker():
    for _ in range(10_000):
        counter.increment()


threads = [
    threading.Thread(target=worker)
    for _ in range(4)
]


for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


print("Final counter:", counter.get_value())


# Explanation:
# SafeCounter encapsulates both the shared value and the lock protecting that value.
# Every thread calls increment(), but the actual modification happens inside a locked section.
# Only one thread can modify the counter at a time.
# get_value() also uses the same lock when reading the value.
# Four worker threads each perform 10,000 increments.
# Because access is synchronized, the final counter represents all completed increments safely.

# Real-Life Use:
# Thread-safe classes are useful when concurrent workers need controlled access to shared application state while keeping synchronization details inside the class.