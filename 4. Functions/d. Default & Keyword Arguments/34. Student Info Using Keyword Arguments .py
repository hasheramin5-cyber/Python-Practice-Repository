# A Program to print student information using keyword arguments.

def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_info(course="Information Technology", age=20, name="Hasher")

# Explanation:
# The program defines a function that accepts three parameters. Instead of passing arguments in order, keyword arguments are used to specify which value belongs to each parameter. This makes function calls easier to read and avoids mistakes caused by argument order.