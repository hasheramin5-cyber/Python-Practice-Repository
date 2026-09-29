# A Program to synchronize threads using an Event

import threading
import time


ready_event = threading.Event()


def worker():
    print("Worker is waiting for the signal...")

    ready_event.wait()

    print("Worker received the signal.")


def controller():
    time.sleep(2)

    print("Controller is sending the signal.")

    ready_event.set()


worker_thread = threading.Thread(target=worker)
controller_thread = threading.Thread(target=controller)


worker_thread.start()
controller_thread.start()


worker_thread.join()
controller_thread.join()


print("Program finished.")


# Explanation:
# Event is a synchronization mechanism that allows one thread to signal another thread.
# The worker calls wait() and pauses until the event is set.
# The controller waits for two seconds to simulate some preparation work.
# It then calls set(), which signals that the required event has occurred.
# The waiting worker continues execution after receiving the signal.

# Real-Life Use:
# Events are useful when one thread must wait for another thread to complete preparation or signal that a resource is ready.