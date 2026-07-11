# A Program to demonstrate Tuple Unpacking.

student = ("Hasher", 20, "Python")

name, age, course = student

print("\nName:", name)
print("Age:", age)
print("Course:", course)

# Explanation:
# The program demonstrates tuple unpacking. The tuple contains three values, and Python automatically assigns each value to its corresponding variable. The first value is stored in 'name', the second in 'age', and the third in 'course'. The number of variables must match the number of elements in the tuple. Tuple unpacking makes it easy to extract multiple values at once.