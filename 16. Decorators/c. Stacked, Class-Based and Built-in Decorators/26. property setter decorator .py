# A Program to validate an attribute using a property setter

class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative.")
            return

        self._age = value


student = Student("Donald Duck", 21)

student.age = 22

print("Age:", student.age)

student.age = -5

print("Age:", student.age)


# Explanation:
# The @property decorator creates the getter for the age attribute.
# The @age.setter decorator defines what should happen when a new value is assigned to age.
# Instead of directly changing the internal _age variable, the assignment is handled by the setter method.
# The setter checks whether the provided age is valid.
# Invalid negative values are rejected while valid values update the stored age.
# This provides controlled access to object data.

# Real-Life Use:
# Property setters are useful for validating user data such as age, price, quantity, temperature, and account balances.