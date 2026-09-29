# A Program to implement a producer-consumer pattern

import threading
import queue
import time


data_queue = queue.Queue()


def producer():
    for number in range(1, 6):
        print(f"Producing item: {number}")

        data_queue.put(number)

        time.sleep(0.5)

    data_queue.put(None)


def consumer():
    while True:
        item = data_queue.get()

        if item is None:
            data_queue.task_done()

            break

        print(f"Consuming item: {item}")

        time.sleep(0.8)

        data_queue.task_done()


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)


producer_thread.start()
consumer_thread.start()


producer_thread.join()
consumer_thread.join()


print("Producer-consumer process completed.")


# Explanation:
# The producer creates data and places each item into the thread-safe queue.
# The consumer retrieves items from the same queue and processes them.
# The queue safely coordinates access between the two threads.
# None acts as a sentinel that tells the consumer that the producer has finished creating items.
# The producer and consumer can operate concurrently, so neither needs to directly control the other's execution.

# Real-Life Use:
# Producer-consumer patterns are useful for message processing, data pipelines, background jobs, logging systems, and streaming workflows.