# A Program to create a decorator using *args and **kwargs

def show_arguments(function):
    def wrapper(*args, **kwargs):
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)

        return function(*args, **kwargs)

    return wrapper


@show_arguments
def student_info(name, age, department):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Department: {department}")


student_info("Hasher Amin", 20, department="Information Technology")


# Explanation:
# A decorator may need to work with functions that accept different numbers and types of arguments.
# *args collects positional arguments into a tuple.
# **kwargs collects keyword arguments into a dictionary.
# The wrapper passes both collections to the original function using function(*args, **kwargs).
# This makes the decorator flexible enough to work with many different function signatures.

# Real-Life Use:
# *args and **kwargs are commonly used in reusable decorators for logging, validation, access control, and function tracing.