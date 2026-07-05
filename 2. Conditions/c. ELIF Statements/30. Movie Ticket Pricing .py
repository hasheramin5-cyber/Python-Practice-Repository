# a program to determine movie ticket pricing based on age using conditional statements.

age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 300
elif age <= 59:
    price = 600
else:
    price = 400

print(f"Ticket Price: Rs. {price}")

# Explanation:
# The program prompts the user to input their age. It then uses conditional statements (if, elif, else) to determine the ticket price based on the age of the user. The pricing is as follows:
# - For children under 5 years old, the ticket is free (Rs. 0).
# - For children between 5 and 12 years old, the ticket price is Rs. 300.
# - For adults between 13 and 59 years old, the ticket price is Rs. 600.
# - For seniors aged 60 and above, the ticket price is Rs. 400.