# A Program to search for a number in a list.

numbers = [10, 25, 18, 42, 56, 71]

search = int(input("Enter a number to search: "))

for number in numbers:
    if number == search:
        print("Number Found!")
        break
else:
    print("Number Not Found!")

# Explanation:
# The program searches for a number entered by the user within a list. It checks each element one by one using a for loop. If the number is found, a message is displayed and the loop ends immediately using the break statement. If the loop finishes without finding the number, the else block displays that the number was not found.