# A Program to find whether the given year is a Century Year or not. Taking year input from the user and converting it into an integer

year = int(input("Enter a year: "))

# Checking if the year is completely divisible by 100
# Years that are divisible by 100 are called Century Years
if year % 100 == 0:
    print("Century Year")
else:
    print("Not a Century Year")

# Explanation:
# A Century Year is a year that marks the beginning of a new century. It is always divisible by 100 without leaving any remainder. The modulus operator (%) is used to check the remainder after division. If the remainder is 0, the year is a Century Year; otherwise, it is not.
    