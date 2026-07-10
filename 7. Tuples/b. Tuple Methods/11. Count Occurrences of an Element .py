# A Program to count the occurrences of an element in a tuple.

numbers = (10, 20, 30, 20, 40, 20, 50)

print(f"\nTuple: {numbers}")
number = int(input("Enter a number: "))

count = numbers.count(number)

print("Occurrences:", count)

# Explanation:
# The program uses the count() method to determine how many times a specific element appears in the tuple. The count() method scans every element and returns the total number of matches. This method is useful for analyzing repeated values in data, such as counting votes, survey responses, or duplicate records.