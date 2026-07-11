# A Program to count even and odd numbers in a tuple.

numbers = (10, 15, 22, 33, 40, 51, 68)

print(f"\nTuple: {numbers}")
even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Numbers:", even_count)
print("Odd Numbers:", odd_count)

# Explanation:
# The program visits every element in the tuple and checks whether it is even or odd using the modulus (%) operator. Two separate counters keep track of the totals. This type of categorization is common in data analysis, reporting, and filtering operations where data needs to be grouped into different classes.