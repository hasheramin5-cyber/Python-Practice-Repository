# A Program to process multiple files using a thread pool

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def count_lines(filename):
    path = Path(filename)

    with path.open("r", encoding="utf-8") as file:
        line_count = sum(1 for _ in file)

    return path.name, line_count


files = [
    "file_one.txt",
    "file_two.txt",
    "file_three.txt"
]


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [
        executor.submit(count_lines, filename)
        for filename in files
    ]

    for future in futures:
        try:
            filename, lines = future.result()

            print(f"{filename}: {lines} lines")

        except FileNotFoundError as error:
            print(f"File not found: {error.filename}")


# Explanation:
# count_lines() opens a file and counts the number of lines.
# Each file is submitted as a separate task to the thread pool.
# The executor can process multiple file operations using different worker threads.
# File operations are I/O-bound, meaning threads can be useful while one operation is waiting for the operating system.
# Each Future stores the result or exception associated with its file-processing task.
# The try-except block handles files that do not exist.


# Real-Life Use:
# Thread pools can be useful for processing many files, downloading resources, reading data, and other I/O-bound workloads.