# A Program to create a simple background task scheduler

import threading
import time


def run_task(task_name, delay):
    time.sleep(delay)

    print(f"Running scheduled task: {task_name}")


tasks = [
    ("Backup", 1),
    ("Generate Report", 2),
    ("Send Notification", 3)
]


threads = [
    threading.Thread(
        target=run_task,
        args=(name, delay)
    )
    for name, delay in tasks
]


for thread in threads:
    thread.start()


for thread in threads:
    thread.join()


print("All scheduled tasks completed.")


# Explanation:
# Each task contains a name and a delay representing when the task should execute.
# A separate thread is created for every scheduled task.
# time.sleep() simulates waiting until the scheduled execution time.
# Because every task has its own thread, the scheduler can wait for different tasks concurrently.
# join() ensures that the main program waits until every scheduled task has finished.

# Real-Life Use:
# Background task scheduling can be used for periodic reports, backups, notifications, cleanup jobs, and maintenance tasks.