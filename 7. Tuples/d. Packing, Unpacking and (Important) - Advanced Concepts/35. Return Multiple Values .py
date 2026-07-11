# A Program to Return multiple values from a Function.

def student():
    return "Hasher", 20, "Python"

name, age, course = student()

print("\nName:", name)
print("Age:", age)
print("Course:", course)

# Explanation:
# The function returns three values. Python automatically packs these values into a tuple when the return statement executes. Later, when the function is called, the returned tuple is unpacked into the variables 'name', 'age', and 'course'. This technique allows functions to return multiple pieces of information in a clean and readable way.