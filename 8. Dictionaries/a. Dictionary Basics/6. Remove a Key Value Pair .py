# A Program to remove a key-value pair from a dictionary.

student = {
    "name": "Hasher",
    "age": 20,
    "course": "Python"
}

del student["course"]

print(student)

# Explanation:
# The program first creates a dictionary containing three key-value pairs. The del statement searches for the key "course" and removes both the key and its associated value from the dictionary. After deletion, the dictionary contains only the remaining key-value pairs, which are then displayed.

# Real-Life Use:
# Removing dictionary items is useful when deleting user data, removing expired records, or clearing unnecessary information from applications.