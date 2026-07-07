# A Program to exit a menu when the user chooses the Exit option.

while True:
    print("\n1. Start")
    print("2. About")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Program Started.")
    elif choice == "2":
        print("This is a sample menu.")
    elif choice == "3":
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice.")

# Explanation:
# The program repeatedly displays a simple menu using an infinite while loop. The user can choose different options, and the menu continues to appear until the Exit option is selected. When the user enters option 3, the break statement terminates the loop and ends the program.