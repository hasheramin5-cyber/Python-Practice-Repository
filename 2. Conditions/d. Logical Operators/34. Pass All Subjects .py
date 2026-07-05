# A Program to check if a student has passed all subjects based on their marks in Math, English, and Science.

math = int(input("\nEnter the Math Marks: "))
english = int(input("Enter the English Marks: "))
science = int(input("Enter the Science Marks: "))

if math >= 40 and english >= 40 and science >= 40:
    print("Congratulations! You Are Passed in All Subjects.")
else:
    print("Best of Luck for Next Time, You are Failed in One or More Subjects.")
    
# Explanation:
# The code checks if a student has passed all subjects based on their marks in Math, English, and Science. The user is prompted to input their marks for each subject. The program then checks if the marks in all three subjects are 40 or above. If all conditions are met, it prints "Congratulations! You Are Passed in All Subjects." Otherwise, it prints "Best of Luck for Next Time, You are Failed in One or More Subjects."