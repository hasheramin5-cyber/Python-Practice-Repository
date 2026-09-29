# A Program to stop a worker thread gracefully

import threading
import time


stop_event = threading.Event()


def worker():
    while not stop_event.is_set():
        print("Worker is processing...")

        time.sleep(0.5)

    print("Worker received shutdown signal.")


thread = threading.Thread(target=worker)

thread.start()

time.sleep(2)

print("Requesting worker shutdown...")

stop_event.set()

thread.join()

print("Worker stopped safely.")


# Explanation:
# A worker thread may need to run continuously until the application requests it to stop.
# The Event object provides a safe way to communicate that shutdown request.
# The worker repeatedly checks is_set().
# While the event is not set, the worker continues processing.
# The main thread eventually calls set(), changing the event state.
# The worker notices the signal, exits its loop, and finishes.
# join() ensures the main thread waits for the worker to stop.

# Real-Life Use:
# Graceful shutdown is useful for background workers, monitoring services, servers, and long-running applications.