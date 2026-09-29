# A Program to create a simple reusable worker pool

import threading
import queue
import time


class WorkerPool:
    def __init__(self, worker_count):
        self.tasks = queue.Queue()

        self.workers = [
            threading.Thread(target=self.worker)
            for _ in range(worker_count)
        ]

        for thread in self.workers:
            thread.start()

    def worker(self):
        while True:
            task = self.tasks.get()

            if task is None:
                self.tasks.task_done()

                break

            task()

            self.tasks.task_done()

    def submit(self, task):
        self.tasks.put(task)

    def shutdown(self):
        self.tasks.join()

        for _ in self.workers:
            self.tasks.put(None)

        for thread in self.workers:
            thread.join()


def create_task(number):
    def task():
        print(f"Processing task {number}")

        time.sleep(0.5)

        print(f"Task {number} completed.")

    return task


pool = WorkerPool(3)


for number in range(1, 7):
    pool.submit(create_task(number))


pool.shutdown()

print("Worker pool stopped.")


# Explanation:
# WorkerPool manages a fixed number of worker threads and a shared task queue.
# Tasks are added using submit().
# Worker threads continuously retrieve tasks from the queue and execute them.
# The number of workers remains fixed even when many tasks are submitted.
# shutdown() waits for queued work to finish and then sends sentinel values to stop the workers.
# This creates a reusable pattern for processing many tasks with a controlled number of threads.

# Real-Life Use:
# Worker pools are useful for servers, job processors, automation systems, and applications with many background tasks.