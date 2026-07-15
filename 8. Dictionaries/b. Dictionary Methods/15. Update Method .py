# A Program to update a Dictionary using the update() method.

student = {
    "name": "Hasher",
    "age": 20
}

student.update({"course": "Python", "city": "Lahore"})

print(student)

# Explanation:
# The program creates a dictionary and then calls the update() method. Python reads the new dictionary passed to update() and adds each key-value pair to the original dictionary. If a key already exists, its value is replaced. If the key does not exist, Python creates a new key-value pair. Finally, the updated dictionary is displayed.

# Real-Life Use:
# The update() method is useful when combining user information, updating settings, or adding new records to existing data.