# a program to check if a character is a vowel or consonant using conditional statements.

character = input("\nEnter a single character: ").lower()

if character in "aeiou":
    print("It is a vowel.")
else:
    print("It is a consonant.")
    
# Explanation:
# The program prompts the user to input a character. It then converts the character to lowercase using the `lower()` method to ensure that the comparison is case-insensitive. The program checks if the character is present in the string "aeiou", which contains all the vowels. If the character is found in this string, it prints that it is a vowel; otherwise, it prints that it is a consonant.