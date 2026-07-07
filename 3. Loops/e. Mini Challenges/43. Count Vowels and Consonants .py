# A Program to count the number of vowels and consonants in a string.

text = input("Enter a string: ").lower()

vowels = 0
consonants = 0

for character in text:
    if character.isalpha():
        if character in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)

# Explanation:
# The program counts the vowels and consonants in a string entered by the user. It checks each character one by one and first confirms that it is an alphabet. If the character is a vowel, the vowel counter is increased; otherwise, the consonant counter is increased. The final counts are displayed after the loop finishes.