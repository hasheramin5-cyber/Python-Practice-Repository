# A Program to iterate through dictionary keys

student = {
    "name": "Hasher",
    "age": 21,
    "semester": 5
}

student_iterator = iter(student)

for key in student_iterator:
    print(key)


# Explanation:
# When iter() is called directly on a dictionary, the iterator is created over its keys.

# The for loop therefore retrieves:
# name
# age
# semester

# Dictionary values are not returned in this example because iteration over a dictionary itself operates on its keys.

# Real-Life Use:
# Dictionary iteration is useful for processing keys in configuration data, records, and structured objects.