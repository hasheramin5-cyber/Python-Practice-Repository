# A Program to calculate the grade of a student based on their score using conditional statements.

marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    
# Explanation:
# The program prompts the user to input their marks. It then uses conditional statements (if, elif, else) to determine the grade based on the marks. The program checks the marks against different ranges and assigns a grade accordingly. If the marks are 90 or above, it assigns Grade A; if they are between 80 and 89, it assigns Grade B; if they are between 70 and 79, it assigns Grade C; if they are between 60 and 69, it assigns Grade D; and if they are below 60, it assigns Grade F.