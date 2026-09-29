# A Program to process tasks using a thread-safe queue

import threading
import queue
import time


task_queue = queue.Queue()


def worker():
    while True:
        task = task_queue.get()

        if task is None:
            task_queue.task_done()

            break

        print(f"Processing: {task}")

        time.sleep(0.5)

        print(f"Completed: {task}")

        task_queue.task_done()


workers = [
    threading.Thread(target=worker)
    for _ in range(2)
]


for worker_thread in workers:
    worker_thread.start()


for number in range(1, 6):
    task_queue.put(f"Task {number}")


task_queue.join()


for _ in workers:
    task_queue.put(None)


for worker_thread in workers:
    worker_thread.join()


print("All tasks completed.")


# Explanation:
# queue.Queue provides a thread-safe way to exchange tasks between threads.
# The main thread places tasks into task_queue using put().
# Worker threads repeatedly retrieve tasks using get().
# After completing a task, a worker calls task_done().
# task_queue.join() makes the main thread wait until all queued tasks have been marked as completed.
# None is used as a sentinel value to tell each worker that no more tasks are available.
# Finally, the worker threads are joined before the program exits.

# Real-Life Use:
# Queues are useful for background workers, job processing, producer-consumer systems, and task scheduling.