# A Program to identify the currently running thread

import threading


def show_thread():
    current = threading.current_thread()

    print("Thread name:", current.name)


thread = threading.Thread(
    target=show_thread,
    name="WorkerThread"
)


thread.start()

thread.join()

print("Main thread:", threading.current_thread().name)


# Explanation:
# threading.current_thread() returns the Thread object that is currently executing.
# Inside show_thread(), it therefore returns the worker thread running that function.
# The thread is given a custom name when it is created.
# The main program also calls current_thread(), but at that point the current thread is the main thread.
# This demonstrates that different parts of a program can identify the thread in which they are executing.

# Real-Life Use:
# Current-thread information is useful for debugging, logging, monitoring, and understanding concurrent programs.