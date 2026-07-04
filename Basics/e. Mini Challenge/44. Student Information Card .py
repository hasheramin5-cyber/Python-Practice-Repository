# Simple Student Information Card in Python.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
course = input("Enter your course: ")

print("\n===== Student Information Card =====")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"City   : {city}")
print(f"Course : {course}")

# Explaination:
# In this code snippet, we take the student's name, age, city, and course as input from the user. We then print a formatted student information card displaying the collected information. The f-strings are used to format the output neatly.