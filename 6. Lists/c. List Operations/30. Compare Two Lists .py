# A Program to compare two lists.

list1 = [10, 20, 30]
list2 = [10, 847, 30]

print(f"\nList1: {list1} \nList2: {list2}")

if list1 == list2:
    print("Both lists are equal.")
else:
    print("The lists are not equal.")

# Explanation:
# The program compares two lists using the equality operator (==). Two lists are considered equal if they contain the same elements in the same order. If either the values or the order differ, the lists are considered different.