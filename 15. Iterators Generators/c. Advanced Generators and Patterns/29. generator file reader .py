# A Program to read a file line by line using a generator

def read_file_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


file_name = "sample.txt"

for line in read_file_lines(file_name):
    print(line)


# Explanation:
# The read_file_lines() function uses a generator to read a file one line at a time.
# The open() function opens the file using a context manager.
# The for loop retrieves each line from the file.
# Instead of reading the complete file into memory, yield returns one line at a time.
# The strip() method removes unnecessary whitespace and newline characters from each line.
# The file is automatically closed when the with block ends.

# Real-Life Use:
# Line-by-line generators are useful for processing large log files, CSV files, text files, and streaming data without loading the entire file into memory.