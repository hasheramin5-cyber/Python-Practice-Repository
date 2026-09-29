# A Program to pass arguments to a thread

import threading


def greet(name, message):
    print(f"{message}, {name}!")


thread = threading.Thread(
    target=greet,
    args=("Hasher", "Welcome")
)


thread.start()

thread.join()

print("Greeting thread completed.")


# Explanation:
# A thread can execute a function that requires arguments.
# The args parameter of Thread() receives a tuple containing positional arguments for the target function.
# The tuple contains the name and message values required by greet().
# When start() is called, Python passes those values to the target function.
# join() ensures that the greeting thread completes before the main program continues.

# Real-Life Use:
# Thread arguments are useful when worker threads need to process different files, users, URLs, records, or tasks.