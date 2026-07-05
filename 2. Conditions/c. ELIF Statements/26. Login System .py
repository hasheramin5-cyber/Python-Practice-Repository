# a program to create a simple login system using conditional statements.

username = input("\nEnter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful.")
else:
    print("Invalid Username or Password.")
    
# Explanation:
# The program prompts the user to input a username and password. It then uses a conditional statement (if, else) to check if the entered username and password match the predefined values ("admin" for username and "1234" for password). If both match, it prints "Login Successful"; otherwise, it prints "Invalid Username or Password."
    
