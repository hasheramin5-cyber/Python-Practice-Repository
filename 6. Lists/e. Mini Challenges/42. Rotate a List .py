# A Program to rotate a list to the right.

numbers = [1, 2, 3, 4, 5]

rotated_list = [numbers[-1]] + numbers[:-1]

print("Original List:", numbers)
print("Rotated List:", rotated_list)

# Explanation:
# The program moves the last element of the list to the beginning while keeping the remaining elements in the same order. This operation is known as list rotation and is used in scheduling systems, circular queues, and many algorithm problems that require cyclic movement of data.