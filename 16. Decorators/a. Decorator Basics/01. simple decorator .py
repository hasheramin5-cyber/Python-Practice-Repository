# A Program to create a simple decorator

def greeting_decorator(function):
    def wrapper():
        print("Welcome to Python!")

        function()

    return wrapper


@greeting_decorator
def show_message():
    print("Learning decorators is really interesting.")


show_message()


# Explanation:
# A decorator is a function that modifies or extends the behavior of another function without changing its original code.
# greeting_decorator() receives show_message() as its argument.
# Inside the decorator, the wrapper() function is created.
# The wrapper() prints a message before calling the original show_message() function.
# The @greeting_decorator syntax applies the decorator to show_message().
# Therefore, calling show_message() actually calls wrapper().

# Real-Life Use:
# Decorators are useful when common behavior needs to be added to multiple functions without repeating the same code.