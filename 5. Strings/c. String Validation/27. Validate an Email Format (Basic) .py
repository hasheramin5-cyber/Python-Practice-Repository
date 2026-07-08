# A Program to perform basic email validation.

email = input("\nEnter your email: ")

if "@" in email and "." in email:
    print("Valid Email Format.")
else:
    print("Invalid Email Format.")

# Explanation:
# The program performs a basic email validation by checking whether the entered email contains both the '@' symbol and a period ('.'). Although this is not a complete email validation, it is sufficient for learning string operations.