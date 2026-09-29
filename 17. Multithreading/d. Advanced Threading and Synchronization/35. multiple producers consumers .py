# A Program to coordinate multiple producers and consumers

import threading
import queue
import time


task_queue = queue.Queue()


def producer(name, start):
    for number in range(start, start + 3):
        task = f"{name} - Task {number}"

        print(f"Producing: {task}")

        task_queue.put(task)

        time.sleep(0.3)


def consumer(name):
    while True:
        task = task_queue.get()

        if task is None:
            task_queue.task_done()

            break

        print(f"{name} processing: {task}")

        time.sleep(0.5)

        print(f"{name} completed: {task}")

        task_queue.task_done()


producers = [
    threading.Thread(
        target=producer,
        args=("Producer 1", 1)
    ),
    threading.Thread(
        target=producer,
        args=("Producer 2", 4)
    )
]


consumers = [
    threading.Thread(
        target=consumer,
        args=("Consumer 1",)
    ),
    threading.Thread(
        target=consumer,
        args=("Consumer 2",)
    )
]


for thread in consumers:
    thread.start()

for thread in producers:
    thread.start()


for thread in producers:
    thread.join()


task_queue.join()


for _ in consumers:
    task_queue.put(None)


for thread in consumers:
    thread.join()


print("All producers and consumers finished.")


# Explanation:
# A thread-safe Queue can support multiple producers and multiple consumers at the same time.
# Both producer threads add tasks to the same queue.
# Both consumer threads retrieve tasks from that queue.
# The queue coordinates access so that producers and consumers can safely work concurrently.
# Producers are joined first to ensure all tasks have been added before the queue is considered complete.
# task_queue.join() waits until every queued task receives a task_done() call.
# Sentinel values then tell each consumer to stop.

# Real-Life Use:
# Multiple producer-consumer systems are useful for job processing, data pipelines, message systems, and automation.