# A Program to store data separately for each thread

import threading


local_data = threading.local()


def worker(name):
    local_data.username = name

    print(
        f"Thread: {threading.current_thread().name} | "
        f"User: {local_data.username}"
    )


thread_one = threading.Thread(
    target=worker,
    args=("Alice",),
    name="Worker-1"
)

thread_two = threading.Thread(
    target=worker,
    args=("Bob",),
    name="Worker-2"
)


thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()


# Explanation:
# threading.local() creates thread-local storage.
# Values stored inside this object are isolated for each individual thread.
# Both worker threads use the same local_data object, but their username values do not overwrite each other.
# Worker-1 stores Alice while Worker-2 stores Bob.
# This is different from normal shared variables, where multiple threads can access the same stored value.

# Real-Life Use:
# Thread-local storage is useful for keeping request data, session information, temporary context, or thread-specific configuration isolated between worker threads.