# A Program to create a thread-safe bank account

import threading


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount

            print(
                f"Deposited {amount}. "
                f"Balance: {self.balance}"
            )

    def withdraw(self, amount):
        with self.lock:
            if amount > self.balance:
                print("Insufficient balance.")

                return False

            self.balance -= amount

            print(
                f"Withdrawn {amount}. "
                f"Balance: {self.balance}"
            )

            return True


account = BankAccount(1000)


threads = [
    threading.Thread(
        target=account.deposit,
        args=(500,)
    ),
    threading.Thread(
        target=account.withdraw,
        args=(200,)
    ),
    threading.Thread(
        target=account.deposit,
        args=(300,)
    ),
    threading.Thread(
        target=account.withdraw,
        args=(400,)
    )
]


for thread in threads:
    thread.start()


for thread in threads:
    thread.join()


print("Final balance:", account.balance)


# Explanation:
# BankAccount stores shared financial data that can be accessed by multiple threads.
# A Lock is created inside the account object so that all balance modifications use the same synchronization mechanism.
# deposit() acquires the lock before changing the balance.
# withdraw() also acquires the same lock before checking and modifying the balance.
# This ensures that the balance cannot be changed by another thread while the current operation is in progress.
# Encapsulating the lock inside the class keeps the synchronization logic close to the shared resource.

# Real-Life Use:
# Thread-safe classes are useful when multiple worker threads need controlled access to shared application state.