# A Program to register functions automatically using a decorator

function_registry = {}


def register(name):
    def decorator(function):
        function_registry[name] = function

        return function

    return decorator


@register("greet")
def greet():
    return "Hello!"


@register("calculate")
def calculate():
    return "Calculation completed."


print("Available functions:", list(function_registry))

print(function_registry["greet"]())
print(function_registry["calculate"]())

# Explanation:
# function_registry is a dictionary that stores registered functions using a name as the key.
# The register() decorator factory receives the name under which the function should be stored.
# When Python creates a decorated function, the decorator immediately adds that function to function_registry.
# The original function is returned unchanged, so it can still be called normally.
# Later, a function can be retrieved from the registry using its registered name.
# This demonstrates how decorators can automatically build collections of functions without manually registering each one.

# Real-Life Use:
# Function registries are useful for command systems, plugin architectures, event handlers, route registration, and extensible applications.