# A Program to return the reverse of a string using a function.

def reverse_string(text):
    reverse = ""

    for character in text:
        reverse = character + reverse

    return reverse

result = reverse_string("Python")
print("Reversed String =", result)

# Explanation:
# The program defines a function that reverses a string using a loop. Each character is added to the beginning of a new string, gradually building the reversed version. The completed reversed string is returned and displayed outside the function.