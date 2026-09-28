# A Program to use the staticmethod built-in decorator

class Calculator:
    @staticmethod
    def add(first, second):
        return first + second

    @staticmethod
    def multiply(first, second):
        return first * second


sum_result = Calculator.add(10, 20)
product_result = Calculator.multiply(5, 4)

print("Sum:", sum_result)
print("Product:", product_result)


# Explanation:
# The @staticmethod decorator creates a method that does not automatically receive the instance or class as its first argument.
# The add() and multiply() methods only need the values required for their calculations.
# These methods can be called directly using the class name.
# A static method is still logically grouped inside the class, even though it does not depend on instance or class state.
# No self or cls parameter is required.

# Real-Life Use:
# Static methods are useful for utility operations that belong conceptually to a class but do not need object-specific data.