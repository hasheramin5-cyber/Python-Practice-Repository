# A Program to repeat a Tuple Multiple Times.

numbers = (1, 2, 3)

print("\nOriginal Tuple:", numbers)

repeat = int(input("Enter the number of times to repeat the tuple: "))

repeated_tuple = numbers * repeat

print("Repeated Tuple:", repeated_tuple)

# Explanation:
# The program repeats the tuple using the multiplication (*) operator. It first displays the original tuple and then asks the user how many times the tuple should be repeated. Python creates a completely new tuple containing the original elements repeated the specified number of times because tuples are immutable. The original tuple remains unchanged. This operation is useful when generating repeated sequences, test datasets, or fixed patterns in programs.