# A Program to calculate the total movie ticket price.

def ticket_price(number_of_tickets, price_per_ticket=500):
    total = number_of_tickets * price_per_ticket
    print("Total Price =", total)

ticket_price(3)
ticket_price(3, 700)

# Explanation:
# The program defines a function that calculates the total cost of movie tickets. By default, each ticket costs 500, but a different price can be provided if needed. The function multiplies the number of tickets by the ticket price and displays the total amount.