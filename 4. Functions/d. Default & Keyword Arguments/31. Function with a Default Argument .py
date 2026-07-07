# A Program to demonstrate a function with a default argument.

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Hasher")

# Explanation:
# The program defines a function with a default argument. If no value is provided when the function is called, Python automatically uses the default value. If a value is provided, it replaces the default value. Default arguments make functions more flexible by allowing optional inputs.