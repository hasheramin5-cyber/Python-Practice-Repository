# A Program to filter transactions using a generator

def transactions():
    data = [
        {"id": 1, "amount": 500},
        {"id": 2, "amount": 2500},
        {"id": 3, "amount": 1200},
        {"id": 4, "amount": 4000}
    ]

    for transaction in data:
        yield transaction


def large_transactions(items, minimum_amount):
    for transaction in items:
        if transaction["amount"] >= minimum_amount:
            yield transaction


transaction_data = transactions()

large_data = large_transactions(transaction_data, 2000)

for transaction in large_data:
    print(transaction)


# Explanation:
# The transactions() generator produces transaction records one at a time.
# Each transaction is represented using a dictionary containing an ID and an amount.
# The large_transactions() generator receives those records and checks their amount.
# Only transactions meeting the minimum amount are passed to the final loop.
# This creates a lazy filtering pipeline where records are processed only when requested.

# Real-Life Use:
# This pattern can be used for transaction processing, financial reports, data filtering, and large record streams.