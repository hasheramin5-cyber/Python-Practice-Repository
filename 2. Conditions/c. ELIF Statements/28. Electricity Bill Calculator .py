# a program to calculate electricity bill based on units consumed using conditional statements.

units = float(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 10
elif units <= 200:
    bill = units * 15
else:
    bill = units * 20

print(f"Electricity Bill: Rs. {bill:.2f}")

# Explanation:
# The program prompts the user to input the number of electricity units consumed. It then uses conditional statements (if, elif, else) to calculate the electricity bill based on the units consumed. The billing rates are as follows:
# - For the first 100 units, the rate is Rs. 10 per unit.
# - For the next 100 units (101 to 200), the rate is Rs. 15 per unit.
# - For units above 200, the rate is Rs. 20 per unit. The program then prints the calculated electricity bill amount formatted to two decimal places.

# Disclaimer: These billing rates are for educational purposes only and may not reflect the actual electricity rates in your area. Please consult your local electricity provider for accurate information.