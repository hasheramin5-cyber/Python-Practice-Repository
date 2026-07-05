character = input("Enter a character: ")

if len(character) == 1 and character.isdigit():
    print("Digit")
else:
    print("Not a Digit")