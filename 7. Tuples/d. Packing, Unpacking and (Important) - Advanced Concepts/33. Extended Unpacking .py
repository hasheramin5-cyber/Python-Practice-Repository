# A Program to demonstrate Extended Tuple unpacking using (*).

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("\nFirst:", first)
print("Middle:", middle)
print("Last:", last)

# Explanation:
# The program demonstrates extended unpacking using the * operator. The first element is assigned to 'first', the last element is assigned to 'last', and all remaining elements are collected into the list 'middle'. The * operator is useful when you do not know exactly how many values will appear between the first and last elements.