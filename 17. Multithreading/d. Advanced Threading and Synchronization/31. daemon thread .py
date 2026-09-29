# A Program to create a daemon thread

import threading
import time


def background_task():
    while True:
        print("Background task is running...")

        time.sleep(1)


thread = threading.Thread(
    target=background_task,
    daemon=True
)


thread.start()

time.sleep(3)

print("Main program finished.")


# Explanation:
# A daemon thread is a background thread that does not prevent the Python program from exiting.
# The daemon=True argument marks the thread as a daemon.
# The background_task() function contains an infinite loop, but the program can still terminate when the main thread finishes.
# When the main program exits, Python does not wait for daemon threads to complete.
# Daemon threads should therefore be used for background work that does not need guaranteed completion.

# Real-Life Use:
# Daemon threads can be useful for background monitoring, status updates, and other supporting tasks that should not keep an application alive.