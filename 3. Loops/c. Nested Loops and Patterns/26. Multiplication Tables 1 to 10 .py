# A Program to print multiplication tables from 1 to 10.

for table in range(1, 11):
    print(f"\nTable of {table}")

    for i in range(1, 11):
        print(f"{table} x {i} = {table * i}")

# Explanation:
# The program prints multiplication tables from 1 to 10 using nested for loops. The outer loop selects each table, while the inner loop prints the multiplication results from 1 to 10. This demonstrates how nested loops can be used to generate repetitive tabular output.