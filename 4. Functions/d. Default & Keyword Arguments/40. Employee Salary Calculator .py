# A Program to calculate an employee's total salary using a default bonus.

def salary_calculator(basic_salary, bonus=5000):
    total_salary = basic_salary + bonus
    print("Total Salary =", total_salary)

salary_calculator(50000)
salary_calculator(50000, 10000)

# Explanation:
# The program defines a function that calculates an employee's total salary by adding a bonus to the basic salary. If no bonus is provided, the default bonus amount is used. Otherwise, the specified bonus replaces the default value.