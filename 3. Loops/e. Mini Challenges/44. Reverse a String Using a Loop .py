# A Program to reverse a string using a loop.

text = input("Enter a string: ")

reverse = ""

for character in text:
    reverse = character + reverse

print("Reversed String:", reverse)

# Explanation:
# The program asks the user to enter a string and reverses it using a loop. During each iteration, the current character is placed before the previously stored characters, gradually building the reversed string. After all characters have been processed, the reversed string is displayed. 