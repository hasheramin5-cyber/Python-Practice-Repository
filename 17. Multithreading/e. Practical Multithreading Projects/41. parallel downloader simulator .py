# A Program to simulate parallel file downloads

from concurrent.futures import ThreadPoolExecutor
import time


def download_file(filename):
    print(f"Starting download: {filename}")

    time.sleep(1)

    print(f"Finished download: {filename}")

    return f"{filename} downloaded"


files = [
    "image.zip",
    "dataset.csv",
    "model.pt",
    "documentation.pdf",
    "backup.zip"
]


with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(download_file, files)

    for result in results:
        print(result)


print("All downloads completed.")


# Explanation:
# Each filename represents a download operation.
# ThreadPoolExecutor creates a pool of worker threads that can process several download operations concurrently.
# The download_file() function uses sleep() to simulate the waiting time normally caused by network I/O.
# executor.map() submits all files to the thread pool.
# Worker threads can process different files at the same time.
# The program waits for all results before printing that the complete download process has finished.

# Real-Life Use:
# This pattern can be used for downloading multiple files, fetching web resources, uploading data, or processing other independent I/O-bound operations.