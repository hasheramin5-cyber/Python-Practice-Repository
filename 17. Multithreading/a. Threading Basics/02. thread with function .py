# A Program to execute a function inside a separate thread

import threading
import time


def download_file():
    print("Download started...")

    time.sleep(2)

    print("Download completed.")


thread = threading.Thread(target=download_file)

thread.start()

print("Main program continues running...")

thread.join()

print("Program finished.")


# Explanation:
# download_file() represents a task that takes some time.
# A Thread object is created with download_file() as its target function.
# start() runs the function in a separate thread.
# While the thread is working, the main program can continue executing other instructions.
# join() is used at the end so the main program waits for the download thread to finish before exiting.

# Real-Life Use:
# This pattern is useful for background downloads, file processing, network operations, and other waiting tasks.