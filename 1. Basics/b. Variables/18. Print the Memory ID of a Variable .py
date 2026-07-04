# Use id to print the memory ID of a variable

# Using the Same value for two different variables will result in the same memory ID for both variables.
a = 10
print("\nThe memory ID of variable 'a' is:", id(a))
b = 10
print("The memory ID of variable 'b' is:", id(b))

#Using Different values for two different variables will result in different memory IDs for both variables.
x = 20
print("\nThe memory ID of variable 'x' is:", id(x))
y = 30
print("The memory ID of variable 'y' is:", id(y))


