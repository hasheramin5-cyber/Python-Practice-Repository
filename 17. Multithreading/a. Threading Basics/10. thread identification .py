# A Program to inspect a thread's identification information

import threading


def show_thread_info():
    current = threading.current_thread()

    print("Thread name:", current.name)
    print("Thread identifier:", current.ident)
    print("Thread alive:", current.is_alive())


thread = threading.Thread(
    target=show_thread_info,
    name="InformationThread"
)


thread.start()

thread.join()

print("Thread alive after join:", thread.is_alive())


# Explanation:
# A Thread object provides information about its current state.
# The name property identifies the thread using a readable name.
# The ident property contains a system-assigned thread identifier while the thread has been started.
# is_alive() tells whether the thread is currently running.
# Inside the worker function, the thread is active, so is_alive() returns True.
# After join() has completed, the thread has finished and is_alive() returns False.

# Real-Life Use:
# Thread information is useful for debugging, monitoring worker threads, and diagnosing concurrency-related issues.