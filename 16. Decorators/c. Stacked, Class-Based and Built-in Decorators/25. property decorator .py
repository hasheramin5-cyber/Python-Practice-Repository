# A Program to create a read-only attribute using the property decorator

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def student_info(self):
        return f"{self.name} is {self.age} years old."


student = Student("Minnie Mouse", 20)

print(student.student_info)


# Explanation:
# The @property decorator allows a method to be accessed like an attribute.
# The student_info() method normally requires parentheses when called as a regular method.
# Because it is decorated with @property, we can access it using student.student_info.
# The property calculates and returns the information whenever it is accessed.
# This allows a class to expose calculated information while keeping the implementation inside the class.

# Real-Life Use:
# Properties are useful for calculated attributes, controlled data access, validation, and creating clean object interfaces.