# A Program to calculate the final price after applying a discount.

def calculate_discount(price, discount=10):
    final_price = price - (price * discount / 100)
    print("Final Price =", final_price)

calculate_discount(5000)
calculate_discount(5000, 20)

# Explanation:
# The program defines a function that calculates the final price after applying a discount. The default discount rate is 10%, but the user can provide a different percentage when calling the function. This demonstrates how default arguments allow flexible calculations.