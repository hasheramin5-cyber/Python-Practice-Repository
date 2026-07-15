# A Program to remove the last inserted item using the popitem() method.

student = {
    "name": "Hasher",
    "age": 20,
    "course": "Python"
}

last_item = student.popitem()

print("Removed Item:", last_item)
print(student)

# Explanation:
# The program creates a dictionary and calls the popitem() method. Python automatically removes the last key-value pair that was added to the dictionary and returns it as a tuple. That tuple is stored in the variable 'last_item'. The remaining dictionary is then displayed.

# Real-Life Use:
# The popitem() method is useful when processing data in reverse insertion order or removing recently added records.