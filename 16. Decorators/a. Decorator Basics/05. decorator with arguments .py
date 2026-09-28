# A Program to create a decorator for a function with arguments

def show_call(function):
    def wrapper(name):
        print("Calling function...")

        function(name)

    return wrapper


@show_call
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
greet("Bob")


# Explanation:
# Decorated functions can also receive arguments.
# The original greet() function expects a name argument.
# Therefore, the wrapper() function must also accept the argument and pass it to the original function.
# When greet("Alice") is called, the decorated wrapper receives "Alice" and then sends it to the original greet() function.
# The same decorator can therefore be used with different argument values.

# Real-Life Use:
# Decorators with arguments are useful when common behavior needs to be added to functions that process input values.