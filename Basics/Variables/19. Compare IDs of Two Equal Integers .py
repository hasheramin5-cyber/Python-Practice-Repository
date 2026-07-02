# Comparing the IDs of two equal integers

a = 10
b = 10

print("\nThe memory ID of variable 'a' is:", id(a))
print("The memory ID of variable 'b' is:", id(b))

print(a is b)  # This will return True since both variables point to the same object in memory