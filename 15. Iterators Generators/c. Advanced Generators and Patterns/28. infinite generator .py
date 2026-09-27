# A Program to create an infinite number generator

def infinite_numbers():
    number = 1

    while True:
        yield number
        number += 1


numbers = infinite_numbers()

for _ in range(5):
    print(next(numbers))


# Explanation:
# An infinite generator is a generator that can continue producing values without having a predefined final limit.
# The while True loop keeps the generator running.
# Each yield returns the current number and pauses execution.
# When next() is called again, the generator resumes, increases the number, and produces the next value.
# The for loop limits how many values we request from the infinite generator.
# Without a stopping condition in the caller, an infinite generator could continue producing values indefinitely.

# Real-Life Use:
# Infinite generators are useful for sequences, event streams, counters, simulations, and continuously generated data.