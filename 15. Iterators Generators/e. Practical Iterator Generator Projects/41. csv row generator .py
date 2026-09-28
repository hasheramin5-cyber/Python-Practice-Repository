# A Program to create a generator for CSV rows

import csv


def read_csv_rows(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            yield row


file_name = "students.csv"

for row in read_csv_rows(file_name):
    print(row)


# Explanation:
# The read_csv_rows() function uses a generator to process a CSV file one row at a time.
# The csv.reader() object itself provides an iterator over the rows in the file.
# Each row is passed to yield, so the caller receives one row at a time.
# The complete CSV file does not need to be loaded into memory.
# The with statement automatically closes the file after processing is complete.

# Real-Life Use:
# This pattern is useful when processing large CSV files, financial records, student data, or other tabular datasets.