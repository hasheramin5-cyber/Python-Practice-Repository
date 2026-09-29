# A Program to generate multiple reports concurrently

from concurrent.futures import ThreadPoolExecutor
import time


reports = [
    "Sales Report",
    "Inventory Report",
    "Customer Report",
    "Performance Report"
]


def generate_report(report_name):
    print(f"Generating: {report_name}")

    time.sleep(1)

    return f"{report_name} generated successfully"


with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [
        executor.submit(generate_report, report)
        for report in reports
    ]

    for future in futures:
        print(future.result())


print("All reports generated.")


# Explanation:
# Each report is treated as an independent task.
# generate_report() simulates the work required to create a report.
# The ThreadPoolExecutor allows several reports to be generated concurrently.
# Every submitted task returns a Future.
# Calling result() retrieves the completed report message.
# The main program waits for all reports before finishing.

# Real-Life Use:
# Concurrent report generation can be useful when an application needs to produce multiple independent reports, exports, summaries, or files.