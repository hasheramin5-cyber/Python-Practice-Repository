# a program to simulate a simple ATM balance checker using conditional statements.

balance = 5000

print("1. Check Balance")
print("2. Withdraw Money")

choice = int(input("Choose an option: "))

if choice == 1:
    print(f"Current Balance: Rs. {balance}")
elif choice == 2:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance -= amount
        print(f"Withdrawal Successful!")
        print(f"Remaining Balance: Rs. {balance}")
    else:
        print("Insufficient Balance")
else:
    print("Invalid Choice")
    

# Explanation:
# The program simulates a simple ATM balance checker. It starts with a predefined balance of Rs. 5000. The user is presented with two options: to check the balance or to withdraw money. If the user chooses to check the balance, the program displays the current balance. If the user chooses to withdraw money, they are prompted to enter the withdrawal amount. The program checks if the withdrawal amount is less than or equal to the current balance. If it is, the withdrawal is successful, and the remaining balance is displayed. If not, an "Insufficient Balance" message is shown. If the user enters an invalid choice, an error message is displayed.