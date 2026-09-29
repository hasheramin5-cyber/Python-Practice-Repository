# A Program to search multiple files concurrently

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def search_file(filename, keyword):
    path = Path(filename)

    try:
        with path.open("r", encoding="utf-8") as file:
            content = file.read()

        found = keyword.lower() in content.lower()

        return path.name, found

    except FileNotFoundError:
        return path.name, False


files = [
    "notes_one.txt",
    "notes_two.txt",
    "notes_three.txt"
]

keyword = "Python"


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [
        executor.submit(search_file, filename, keyword)
        for filename in files
    ]

    for future in futures:
        filename, found = future.result()

        if found:
            print(f"{keyword} found in {filename}")

        else:
            print(f"{keyword} not found in {filename}")


# Explanation:
# search_file() reads one file and checks whether the requested keyword exists in its contents.
# Each file is submitted as an independent task.
# The thread pool can process several file searches at the same time.
# Each Future stores the result returned by its corresponding search operation.
# FileNotFoundError is handled inside the worker so one missing file does not stop the complete search process.

# Real-Life Use:
# Concurrent file searching can be useful for log analysis, document searching, codebase scanning, and large collections of text files.