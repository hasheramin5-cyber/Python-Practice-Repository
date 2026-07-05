# A Program to check if a person is eligible to vote based on age and nationality.

age = int(input("\nEnter your age: "))
nationality = input("Enter your nationality: ")

if age >= 18 and (nationality.lower() == "pakistani" or nationality.lower() == "pakistan" or nationality.lower() == "pakistani citizen" or nationality.lower() == "pakistani national"):
  
    print("Eligible to Vote.")
else:
    print("Not Eligible to Vote.")
    
# Explanation:
# The code checks if a person is eligible to vote based on their age and nationality. The user is prompted to input their age and nationality. The program then checks if the age is 18 or above and if the nationality matches any of the specified strings (case-insensitive). If both conditions are met, it prints "Eligible to Vote." Otherwise, it prints "Not Eligible to Vote."