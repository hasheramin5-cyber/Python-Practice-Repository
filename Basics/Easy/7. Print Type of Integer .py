# Print the type of an integer

a = 100
print("\nThe value of a is:", a)
print(type(a))
print("The type of a is:", type(a))
print("The type of a is:", type(a).__name__)  

# Here "__name__" is used to get the name of the type as a string, which will print "int" for an integer.