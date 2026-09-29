# A Program to create and run a basic thread

import threading


def show_message():
    print("Hello from the thread!")


thread = threading.Thread(target=show_message)

thread.start()

thread.join()

print("Main program finished.")


# Explanation:
# The threading module provides tools for creating and managing threads in Python.
# Thread() creates a new thread object.
# The target parameter tells the thread which function it should execute.
# start() begins execution of the new thread.
# join() makes the main program wait until the thread finishes its work.
# After the thread completes, the main program continues.

# Real-Life Use:
# Basic threads are useful when an application needs to perform work independently from the main program flow.