# A Program to build a simple multithreaded job system

import threading
import queue
import time


class JobSystem:
    def __init__(self, worker_count):
        self.jobs = queue.Queue()

        self.workers = [
            threading.Thread(target=self.worker)
            for _ in range(worker_count)
        ]

        for worker in self.workers:
            worker.start()

    def worker(self):
        while True:
            job = self.jobs.get()

            if job is None:
                self.jobs.task_done()

                break

            job()

            self.jobs.task_done()

    def submit(self, job):
        self.jobs.put(job)

    def shutdown(self):
        self.jobs.join()

        for _ in self.workers:
            self.jobs.put(None)

        for worker in self.workers:
            worker.join()


def create_job(number):
    def job():
        print(f"Running job {number}")

        time.sleep(0.5)

        print(f"Job {number} completed")

    return job


job_system = JobSystem(3)


for number in range(1, 8):
    job_system.submit(create_job(number))


job_system.shutdown()

print("Job system shut down.")


# Explanation:
# JobSystem manages a shared queue and a fixed number of worker threads.
# submit() places a job into the queue.
# Worker threads continuously retrieve jobs and execute them.
# The queue provides safe communication between the main thread and workers.
# shutdown() first waits for all submitted jobs to finish.
# Sentinel values are then added to tell the workers to stop.
# Finally, join() ensures every worker exits cleanly.

# Real-Life Use:
# Job systems are useful for background processing, web servers, automation platforms, task queues, and application worker services.