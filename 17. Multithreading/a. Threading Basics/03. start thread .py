# A Program to start a thread and observe its execution

import threading


def print_numbers():
    for number in range(1, 6):
        print("Thread:", number)


thread = threading.Thread(target=print_numbers)

print("Starting thread...")

thread.start()

thread.join()

print("Thread has finished.")


# Explanation:
# The print_numbers() function contains the work that the new thread will perform.
# Thread() creates the thread but does not start it yet.
# start() changes the thread from a created state to an actively running state.
# The thread then executes print_numbers().
# join() waits until all five numbers have been processed.
# The main program continues after the thread finishes.

# Real-Life Use:
# Explicitly starting threads is useful when an application needs to control when background work begins.