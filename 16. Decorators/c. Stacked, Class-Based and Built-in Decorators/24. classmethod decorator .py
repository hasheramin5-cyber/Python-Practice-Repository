# A Program to use the classmethod built-in decorator

class Student:
    school_name = "Future Academy"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school

    def display(self):
        print(f"Student: {self.name}")
        print(f"School: {self.school_name}")


student = Student("Mickey Mouse")

student.display()

Student.change_school("Modern Academy")

student.display()


# Explanation:
# The @classmethod decorator creates a method that receives the class itself as the first argument.
# By convention, this first argument is named cls.
# change_school() uses cls to access and modify the class variable school_name.
# Because school_name belongs to the class, the change affects the value used by Student objects.
# A class method can be called using either the class or an instance, although it is commonly called through the class.

# Real-Life Use:
# Class methods are useful for modifying shared class state, creating alternative constructors, and working with data common to all objects.