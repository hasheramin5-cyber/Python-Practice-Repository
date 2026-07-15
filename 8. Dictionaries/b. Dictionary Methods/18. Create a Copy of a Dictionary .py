# A Program to create a copy of a dictionary.

student = {
    "name": "Hasher",
    "age": 20,
    "course": "Python"
}

student_copy = student.copy()

print("Original Dictionary:", student)
print("Copied Dictionary:", student_copy)

# Explanation:
# The program creates a dictionary and then calls the copy() method. Python creates a new dictionary containing the same key-value pairs as the original. The copied dictionary is stored in the variable 'student_copy'. Changes made to one dictionary will not affect the other because they are separate objects.

# Real-Life Use:
# Creating copies is useful when you need a backup before modifying important data or when working with temporary versions of records.