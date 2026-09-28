# A Program to build a reusable input validation system

from functools import wraps


def validate_registration(function):
    @wraps(function)
    def wrapper(name, age):
        if not name.strip():
            print("Name cannot be empty.")
            return

        if not isinstance(age, int) or age < 18:
            print("Age must be an integer of 18 or above.")
            return

        return function(name, age)

    return wrapper


@validate_registration
def register_user(name, age):
    print(f"User registered: {name}, Age: {age}")


register_user("Hasher", 21)

register_user("", 21)

register_user("Amin", 15)


# Explanation:
# The validate_registration() decorator centralizes input validation for the registration function.
# The wrapper first checks whether the name contains useful text after removing surrounding whitespace.
# It then checks whether age is an integer and whether it satisfies the minimum age requirement.
# Invalid input prevents the original function from executing.
# Valid input is passed to register_user() normally.
# This keeps validation separate from the main registration operation.

# Real-Life Use:
# Validation decorators are useful for forms, registration systems, API endpoints, configuration functions, and data-processing pipelines.