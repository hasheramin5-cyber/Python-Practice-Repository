# A Program to Retrieve a value using the get() method.

student = {
    "name": "Hasher",
    "age": 20,
    "course": "Python"
}

key = input("Enter a key: ")

value = student.get(key)

print("Value:", value)

# Explanation:
# The program asks the user to enter a key and stores it in the variable 'key'. The get() method then searches for that key inside the dictionary. If the key exists, its corresponding value is returned. If the key does not exist, get() returns None instead of causing an error. This makes get() safer than directly accessing values using square brackets.

# Real-Life Use:
# The get() method is commonly used when working with user input, APIs, and optional data where a key may or may not exist.