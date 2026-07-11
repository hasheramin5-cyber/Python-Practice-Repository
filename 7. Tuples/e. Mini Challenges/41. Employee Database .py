# A Program to Store Employee Information using Tuples.

employees = (
    (101, "Bill Faruki", "Developer"),
    (102, "Hasher Amin", "Designer"),
    (103, "Adil Chanda", "Manager")
)

print("Employee Database:\n")

for emp_id, name, department in employees:
    print(f"ID: {emp_id} | Name: {name} | Department: {department}")

# Explanation:
# The program stores employee records as nested tuples. Each employee has an ID, name, and department. During each iteration, Python unpacks one employee's tuple into three variables. Using tuples for employee records helps protect important information from accidental modification because tuples are immutable.