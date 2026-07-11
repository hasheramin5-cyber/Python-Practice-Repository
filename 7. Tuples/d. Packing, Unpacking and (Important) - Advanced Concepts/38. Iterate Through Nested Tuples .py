# A Program to Iterate through Nested Tuples.

students = (
    ("Hasher", 20),
    ("Ali", 22),
    ("Sara", 21)
)

for name, age in students:
    print(name, "-", age)

# Explanation:
# The program uses a for loop to iterate through the outer tuple. During each iteration, Python automatically unpacks the current inner tuple into the variables 'name' and 'age'. This makes the code shorter, cleaner, and easier to read when working with structured collections of data.