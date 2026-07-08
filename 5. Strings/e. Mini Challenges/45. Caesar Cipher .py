# A Program to encrypt a message using the Caesar Cipher.

# Definition:
# The Caesar Cipher is an encryption technique in which each letter is shifted by a fixed number of positions in the alphabet.

text = input("\nEnter a message: ")

shift = int(input("Enter the shift value: "))

encrypted = ""

for character in text:
    if character.isalpha():
        if character.islower():
            encrypted += chr((ord(character) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += chr((ord(character) - ord('A') + shift) % 26 + ord('A'))
    else:
        encrypted += character

print("\nEncrypted Message is:", encrypted)

# Explanation:
# The program encrypts a message using the Caesar Cipher. Every alphabetic character is shifted by the specified number of positions while preserving uppercase and lowercase letters. Non-alphabetic characters remain unchanged.