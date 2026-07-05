secret_number = 7

guess = int(input("\nGuess the number (1-10): "))

if guess == secret_number:
    print("Congratulations! You guessed correctly.")
else:
    print("Wrong guess.")