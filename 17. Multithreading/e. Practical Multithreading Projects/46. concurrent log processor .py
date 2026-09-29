# A Program to process log entries concurrently

from concurrent.futures import ThreadPoolExecutor
import time


logs = [
    "INFO: User logged in",
    "ERROR: Database connection failed",
    "INFO: File uploaded",
    "WARNING: Storage almost full",
    "ERROR: Request timeout",
    "INFO: User logged out"
]


def process_log(log):
    time.sleep(0.3)

    if log.startswith("ERROR"):
        category = "ERROR"

    elif log.startswith("WARNING"):
        category = "WARNING"

    else:
        category = "INFO"

    return category, log


with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(
        executor.map(process_log, logs)
    )


summary = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}


for category, log in results:
    summary[category] += 1

    print(f"[{category}] {log}")


print("\nLog Summary:", summary)


# Explanation:
# Each log entry is treated as an independent processing task.
# process_log() identifies the category of the log entry.
# ThreadPoolExecutor processes multiple log entries concurrently.
# The returned category and original message are collected from every task.
# The main thread then builds a summary containing the number of INFO, WARNING, and ERROR messages.

# Real-Life Use:
# Concurrent log processing can help with large application logs, monitoring systems, server logs, and background analysis pipelines.