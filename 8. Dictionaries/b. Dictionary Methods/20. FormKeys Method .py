# A Program to create a Dictionary using the fromkeys() method.

keys = ("name", "age", "course")

student = dict.fromkeys(keys, "Not Available")

print(student)

# Explanation:
# The program first creates a tuple containing three keys. The fromkeys() method then creates a new dictionary using those keys. Every key is assigned the same default value, "Not Available". This is useful when you know the field names in advance but the actual values will be added later.

# Real-Life Use:
# The fromkeys() method is commonly used when creating templates for forms, employee records, user profiles, or configuration files where every field starts with the same default value.