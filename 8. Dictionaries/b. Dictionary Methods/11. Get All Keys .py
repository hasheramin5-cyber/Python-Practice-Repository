# A Program to get all keys from a dictionary.

student = {
    "name": "Hasher",
    "age": 20,
    "course": "Python"
}

keys = student.keys()

print("Dictionary Keys:")
print(keys)

# Explanation:
# The program creates a dictionary named 'student' that stores three key-value pairs. The keys() method is then called on the dictionary. Instead of returning the values, it returns a special object containing only the keys. This object is stored in the variable 'keys' and then displayed using print(). The keys() method is useful when you only need the names of the fields without accessing their corresponding values.

# Real-Life Use:
# The keys() method is commonly used to display available settings, form fields, database columns, or configuration options.