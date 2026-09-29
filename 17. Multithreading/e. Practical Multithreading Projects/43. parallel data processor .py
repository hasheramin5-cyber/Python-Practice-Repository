# A Program to process a dataset using multiple threads

from concurrent.futures import ThreadPoolExecutor
import time


def process_record(record):
    print(f"Processing record {record}")

    time.sleep(0.4)

    return {
        "id": record,
        "processed": True
    }


records = range(1, 11)


with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(
        executor.map(process_record, records)
    )


print("\nProcessed Records:")

for record in results:
    print(record)


# Explanation:
# Each number represents one independent data record.
# process_record() simulates processing work for that record.
# ThreadPoolExecutor distributes the records among multiple worker threads.
# executor.map() collects the returned values in the same order as the original records.
# Because the simulated work is I/O-like, several records can be processed while other threads are waiting.
# The final results contain a processed representation of every record.

# Real-Life Use:
# This pattern can be useful for processing API responses, files, database records, data validation tasks, and other independent I/O-bound records.