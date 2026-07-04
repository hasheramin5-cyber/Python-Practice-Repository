# Print the type of a string

a = "Hello, World!"
print("\nThe value of a is:", a)
print(type(a))
print("The type of a is:", type(a))
print("The type of a is:", type(a).__name__)

# Here "__name__" is used to get the name of the type as a string, which will print "str" for a string.