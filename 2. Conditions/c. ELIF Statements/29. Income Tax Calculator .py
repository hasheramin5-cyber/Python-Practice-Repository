# a program to calculate income tax based on annual income using conditional statements.

income = float(input("Enter your annual income: "))

if income <= 500000:
    tax = 0
elif income <= 1000000:
    tax = income * 0.05
elif income <= 2000000:
    tax = income * 0.10
else:
    tax = income * 0.15

print(f"Income Tax: Rs. {tax:.2f}")

# Explanation:
# The program prompts the user to input their annual income. It then uses conditional statements (if, elif, else) to calculate the income tax based on the income slabs. The tax rates are as follows:
# - For income up to Rs. 5,00,000, the tax is 0%.
# - For income between Rs. 5,00,001 and Rs. 10,00,000, the tax is 5%.
# - For income between Rs. 10,00,001 and Rs. 20,00,000, the tax is 10%.
# - For income above Rs. 20,00,000, the tax is 15%. The program then prints the calculated income tax amount formatted to two decimal places.

# Disclaimer: These tax rates are for educational purposes only and may not reflect the actual tax rates in your country. Please consult a tax professional for accurate information.