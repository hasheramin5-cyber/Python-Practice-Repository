# A Program to process log file lines using a generator

def log_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


def error_lines(lines):
    for line in lines:
        if "ERROR" in line:
            yield line


file_name = "application.log"

all_lines = log_lines(file_name)
errors = error_lines(all_lines)

for error in errors:
    print(error)


# Explanation:
# The log_lines() generator reads the log file one line at a time.
# The error_lines() generator receives those lines and checks whether the word "ERROR" exists.
# Only matching lines are passed forward using yield.
# These two generators form a small processing pipeline.
# The complete log file is never stored in memory.
# Data moves through the pipeline only when the final loop requests the next result.

# Real-Life Use:
# Generator-based log processing is useful for monitoring application logs and finding errors in very large files.