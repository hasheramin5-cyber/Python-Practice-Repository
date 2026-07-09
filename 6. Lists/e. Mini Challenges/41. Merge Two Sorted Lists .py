# A Program to merge two sorted lists.

list1 = [10, 20, 30]
list2 = [15, 25, 35]

print(f"\nList1: {list1} \nList2: {list2}")

merged_list = list1 + list2
print(f"\nMerged List: {merged_list}")
merged_list.sort()

print("Sorted Merged List:", merged_list)

# Explanation:
# The program combines two sorted lists using the + operator and then sorts the resulting list. Merging sorted collections is commonly used in searching, database operations, and sorting algorithms. Later, you'll learn more efficient ways to merge sorted data without sorting again.