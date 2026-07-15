# A Program to check whether a key exists in a Dictionary.

student = {
    "Name": "Hasher",
    "Age": 20,
    "Course": "Python"
}

key = input("Enter a key: ")

if key in student:
    print("Key exists.")
else:
    print("Key does not exist.")

# Explanation:
# The program creates a dictionary and asks the user to enter a key. The entered value is stored in the variable 'key'. The if statement uses the 'in' operator to check whether that key exists in the dictionary. If Python finds the key, the condition becomes True and the first message is printed. Otherwise, the else block executes and informs the user that the key was not found.

# Real-Life Use:
# This technique is widely used before accessing dictionary values to avoid errors when the requested key does not exist.