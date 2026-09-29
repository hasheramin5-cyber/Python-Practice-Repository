# A Program to build a complete multithreaded task manager

from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def execute_task(task):
    task_id, duration = task

    print(f"Task {task_id} started.")

    time.sleep(duration)

    print(f"Task {task_id} completed.")

    return task_id, "Completed"


tasks = [
    (1, 1.0),
    (2, 0.5),
    (3, 1.5),
    (4, 0.8),
    (5, 0.3),
    (6, 1.2)
]


completed_tasks = []


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [
        executor.submit(execute_task, task)
        for task in tasks
    ]

    for future in as_completed(futures):
        task_id, status = future.result()

        completed_tasks.append((task_id, status))

        print(
            f"Manager received result: "
            f"Task {task_id} -> {status}"
        )


print("\nFinal Task Report:")

for task_id, status in sorted(completed_tasks):
    print(f"Task {task_id}: {status}")


# Explanation:
# This program combines several concepts from the previous multithreading exercises.
# ThreadPoolExecutor manages a fixed number of worker threads.
# Each task contains an ID and an execution duration.
# submit() creates a Future for every task.
# as_completed() allows the manager to process results as soon as individual tasks finish instead of waiting for tasks in submission order.
# Completed results are stored in completed_tasks.
# sorted() is used only for the final report so that tasks are displayed in their original numerical order.
# This demonstrates how a real task manager can submit, execute, monitor, and collect concurrent work.

# Real-Life Use:
# Task managers are useful for automation systems, background workers, batch processing, data pipelines, and applications that need to coordinate many independent tasks.