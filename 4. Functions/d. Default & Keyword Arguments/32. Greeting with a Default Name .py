# A Program to greet a user using a default name.

def welcome(name="Friend"):
    print(f"Welcome, {name}!")

welcome()
welcome("Amin")

# Explanation:
# The program defines a function that greets a user. If no name is passed to the function, it uses the default name "Friend". Otherwise, it greets the user with the provided name. This demonstrates another practical use of default arguments.