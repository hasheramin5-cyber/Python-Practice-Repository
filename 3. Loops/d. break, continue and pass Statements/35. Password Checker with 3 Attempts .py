# A Program to check a password with a maximum of three attempts.

correct_password = "python123"

for attempt in range(1, 4):
    password = input("Enter Password: ")

    if password == correct_password:
        print("Access Granted!")
        break
else:
    print("Access Denied!")

# Explanation:
# The program allows the user up to three attempts to enter the correct password. If the entered password matches the predefined password, access is granted and the loop stops using the break statement. If all three attempts are used without entering the correct password, the else block executes and access is denied.