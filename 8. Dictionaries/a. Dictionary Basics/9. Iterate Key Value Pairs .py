# A Program to iterate through dictionary key-value pairs.

student = {
    "name": "Hasher",
    "age": 20,
    "course": "Python"
}

for key, value in student.items():
    print(f"{key}: {value}")

# Explanation:
# The program creates a dictionary and uses the items() method to retrieve both keys and their corresponding values together. During each iteration, Python automatically unpacks one key-value pair into the variables 'key' and 'value'. The loop then prints both pieces of information before moving to the next pair. This continues until every item in the dictionary has been processed.

# Real-Life Use:
# Iterating through key-value pairs is commonly used to display user profiles, generate reports, process JSON data, and work with API responses.