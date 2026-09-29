# A Program to limit concurrent access using a semaphore

import threading
import time


semaphore = threading.Semaphore(2)


def use_resource(worker_name):
    with semaphore:
        print(f"{worker_name} acquired a resource.")

        time.sleep(1)

        print(f"{worker_name} released the resource.")


threads = []

for number in range(5):
    thread = threading.Thread(
        target=use_resource,
        args=(f"Worker {number + 1}",)
    )

    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


print("All workers completed.")


# Explanation:
# A semaphore controls how many threads can access a resource at the same time.
# Semaphore(2) allows a maximum of two threads to enter the protected section concurrently.
# When a thread enters the with semaphore block, one available permit is acquired.
# When the thread leaves the block, the permit is released.
# Other threads wait when all available permits are already being used.

# Real-Life Use:
# Semaphores are useful for limiting access to connection pools, worker resources, database connections, and services with a maximum concurrency limit.