# A Program to convert one currency into another using a fixed exchange rate.

def currency_converter(amount, exchange_rate=278):
    converted_amount = amount * exchange_rate
    print("Converted Amount =", converted_amount)

currency_converter(100)
currency_converter(100, 300)

# Explanation:
# The program defines a function that converts an amount into another currency using a fixed exchange rate. If no exchange rate is provided, the default value is used. Otherwise, the specified exchange rate replaces the default. This example demonstrates how default arguments simplify repeated calculations.