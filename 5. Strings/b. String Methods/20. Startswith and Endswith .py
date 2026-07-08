# A Program to check whether a string starts or ends with a specific value.

text = input("\nEnter a string: ")

start = input("Enter the starting text: ")
end = input("Enter the ending text: ")

print("Starts With:", text.startswith(start))
print("Ends With:", text.endswith(end))

# Explanation:
# The program checks whether a string begins or ends with specified text using the startswith() and endswith() methods. These methods return True if the condition is satisfied; otherwise, they return False.