# A Program to count the occurrences of an element in a list.

numbers = [10, 20, 10, 30, 10, 40, 20]

number = int(input("\nEnter a number: "))

print("\nList:", numbers)
print(f"Occurrence of {number} in List is:", numbers.count(number))

# Explanation:
# The program counts how many times a specified element appears in the list using the count() method and displays the total number of occurrences.