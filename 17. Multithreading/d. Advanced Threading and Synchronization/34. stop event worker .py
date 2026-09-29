# A Program to control a worker using start and stop events

import threading
import time


start_event = threading.Event()
stop_event = threading.Event()


def worker():
    print("Worker is waiting to start...")

    start_event.wait()

    print("Worker started.")

    while not stop_event.is_set():
        print("Worker is processing tasks...")

        time.sleep(0.5)

    print("Worker stopped.")


thread = threading.Thread(target=worker)

thread.start()

time.sleep(1)

print("Sending start signal.")

start_event.set()

time.sleep(2)

print("Sending stop signal.")

stop_event.set()

thread.join()

print("Program finished.")


# Explanation:
# This program uses two Event objects to control a worker's lifecycle.
# The worker first waits for start_event to be set.
# Once the main thread calls start_event.set(), the worker begins processing.
# The worker continues until stop_event is set.
# The main thread later sends the shutdown signal by calling stop_event.set().
# This separates starting and stopping signals into two independent synchronization mechanisms.

# Real-Life Use:
# Start and stop events are useful for worker services, background processing systems, and applications where task execution needs explicit lifecycle control.