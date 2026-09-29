# A Program to synchronize multiple threads using a barrier

import threading
import time


barrier = threading.Barrier(3)


def worker(name, delay):
    print(f"{name} started.")

    time.sleep(delay)

    print(f"{name} reached the barrier.")

    barrier.wait()

    print(f"{name} passed the barrier.")


threads = [
    threading.Thread(
        target=worker,
        args=("Worker 1", 1)
    ),
    threading.Thread(
        target=worker,
        args=("Worker 2", 2)
    ),
    threading.Thread(
        target=worker,
        args=("Worker 3", 3)
    )
]


for thread in threads:
    thread.start()


for thread in threads:
    thread.join()


print("All workers completed.")


# Explanation:
# Barrier allows a fixed number of threads to wait until all participating threads reach the same synchronization point.
# Barrier(3) means three threads must reach the barrier.
# Each worker performs its own task and then calls barrier.wait().
# Faster workers wait at the barrier for slower workers.
# Once all three workers arrive, they are released and continue execution.
# This creates a synchronization checkpoint for multiple threads.

# Real-Life Use:
# Barriers are useful when several workers must complete one phase of processing before any of them starts the next phase.