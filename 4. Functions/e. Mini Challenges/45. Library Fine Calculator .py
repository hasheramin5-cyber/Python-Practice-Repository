# A Program to calculate the library fine using a function.

def calculate_fine(days):
    fine_per_day = 20
    return days * fine_per_day

late_days = int(input("\nEnter the number of late days: "))

print("Library Fine =>", calculate_fine(late_days),"Rs.")

# Explanation:
# The program defines a function that calculates the library fine based on the number of late days. The function multiplies the number of days by the fixed fine per day and returns the total amount.