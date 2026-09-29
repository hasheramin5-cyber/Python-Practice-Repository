# A Program to build a thread-safe inventory system

import threading


class Inventory:
    def __init__(self):
        self.stock = {}
        self.lock = threading.Lock()

    def add_item(self, item, quantity):
        with self.lock:
            self.stock[item] = self.stock.get(item, 0) + quantity

    def remove_item(self, item, quantity):
        with self.lock:
            available = self.stock.get(item, 0)

            if available >= quantity:
                self.stock[item] = available - quantity

                return True

            return False

    def show_stock(self):
        with self.lock:
            return self.stock.copy()


inventory = Inventory()

inventory.add_item("Laptop", 10)


def purchase():
    if inventory.remove_item("Laptop", 1):
        print("Laptop purchased.")

    else:
        print("Laptop unavailable.")


threads = [
    threading.Thread(target=purchase)
    for _ in range(6)
]


for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


print("Remaining stock:", inventory.show_stock())


# Explanation:
# Inventory contains shared stock data that multiple threads may access at the same time.
# The Lock protects both adding and removing inventory.
# When a purchase occurs, checking the available quantity and updating the stock happen inside the same locked section.
# This prevents two threads from incorrectly modifying the same inventory value at the same time.
# show_stock() returns a copy so callers do not directly manipulate the internal shared dictionary.

# Real-Life Use:
# Thread-safe inventory systems are useful for e-commerce, warehouse management, ticket booking, and shared resource tracking systems.