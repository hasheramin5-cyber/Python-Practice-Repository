# A Program to find the position of a substring in a string.

text = input("\nEnter a string: ")

search = input("Enter the substring to find: ")

position = text.find(search)

if position != -1:
    print("Substring found at index:", position)
else:
    print("Substring not found.")

# Explanation:
# The program searches for a substring using the find() method. If the substring exists, the method returns the index of its first occurrence. If it is not found, the method returns -1, allowing the program to display an appropriate message.