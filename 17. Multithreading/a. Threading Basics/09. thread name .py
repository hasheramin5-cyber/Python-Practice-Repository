# A Program to assign and change a thread name

import threading


def worker():
    current = threading.current_thread()

    print("Running thread:", current.name)

    current.name = "UpdatedWorker"

    print("New thread name:", current.name)


thread = threading.Thread(
    target=worker,
    name="InitialWorker"
)


print("Before start:", thread.name)

thread.start()

thread.join()

print("After completion:", thread.name)


# Explanation:
# Every Thread object has a name that can be used to identify it.
# A custom name can be provided when the thread is created.
# Inside worker(), current_thread() retrieves the currently running thread.
# The name property can also be changed during execution.
# After the thread finishes, the Thread object still contains its updated name.

# Real-Life Use:
# Meaningful thread names make logs and debugging output much easier to understand in applications using many threads.