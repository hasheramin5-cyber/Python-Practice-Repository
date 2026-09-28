# A Program to generate password attempts from a collection

def password_attempts(passwords):
    for password in passwords:
        yield password


possible_passwords = [
    "python123",
    "admin123",
    "letmein",
    "secure123"
]

attempts = password_attempts(possible_passwords)

for attempt in attempts:
    print("Trying:", attempt)


# Explanation:
# The password_attempts() function demonstrates how a generator can provide candidate values one at a time.
# The function receives a collection and yields each value sequentially.
# Only one value is being retrieved from the generator at a time.
# The generator itself does not determine whether an attempt is successful; it simply controls how values are produced.
# This example focuses on generator mechanics rather than performing any real authentication or password testing.

# Real-Life Use:
# The same generator pattern can be used for safe test data, test cases, configuration candidates, or controlled simulations.