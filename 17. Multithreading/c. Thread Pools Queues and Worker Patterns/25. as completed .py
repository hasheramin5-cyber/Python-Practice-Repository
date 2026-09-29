# A Program to process Future results as tasks complete

from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def process_task(task_number):
    time.sleep(task_number * 0.5)

    return f"Task {task_number} completed."


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [
        executor.submit(process_task, number)
        for number in [3, 1, 2]
    ]

    for future in as_completed(futures):
        print(future.result())


# Explanation:
# as_completed() yields Future objects as soon as their associated tasks finish.
# This means results do not have to be processed in the same order in which tasks were submitted.
# A task that finishes early can be handled immediately, even if another task submitted before it is still running.
# This is different from simply calling result() on futures in submission order.

# Real-Life Use:
# as_completed() is useful when completed results should be processed immediately, especially when tasks have different execution times.