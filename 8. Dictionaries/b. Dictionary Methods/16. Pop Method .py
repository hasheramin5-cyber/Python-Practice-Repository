# A Program to remove an item using the pop() method.

student = {
    "name": "Hasher",
    "age": 20,
    "course": "Python"
}

removed_value = student.pop("course")

print("Removed Value:", removed_value)
print(student)

# Explanation:
# The program creates a dictionary and calls the pop() method with the key "course". Python searches for that key, removes it from the dictionary, and returns its value. The returned value is stored in the variable 'removed_value' and then printed. The updated dictionary is displayed after the removal.

# Real-Life Use:
# The pop() method is useful when removing completed tasks, expired records, or unnecessary information while still keeping the removed value.