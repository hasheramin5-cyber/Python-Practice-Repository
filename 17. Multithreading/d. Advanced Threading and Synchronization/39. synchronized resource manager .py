# A Program to create a synchronized resource manager

import threading


class ResourceManager:
    def __init__(self):
        self.resources = []
        self.lock = threading.Lock()

    def add_resource(self, resource):
        with self.lock:
            self.resources.append(resource)

            print(f"Added: {resource}")

    def remove_resource(self, resource):
        with self.lock:
            if resource in self.resources:
                self.resources.remove(resource)

                print(f"Removed: {resource}")

    def show_resources(self):
        with self.lock:
            print("Resources:", self.resources)


manager = ResourceManager()


threads = [
    threading.Thread(
        target=manager.add_resource,
        args=("Resource A",)
    ),
    threading.Thread(
        target=manager.add_resource,
        args=("Resource B",)
    ),
    threading.Thread(
        target=manager.add_resource,
        args=("Resource C",)
    )
]


for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


manager.show_resources()


# Explanation:
# ResourceManager stores a shared list that multiple threads may modify.
# A Lock is stored inside the class so every operation uses the same synchronization mechanism.
# add_resource() acquires the lock before changing the list.
# remove_resource() follows the same rule.
# show_resources() also uses the lock so that the list is accessed safely while other operations are controlled.
# Encapsulating synchronization inside the class makes it harder for callers to accidentally access the shared resource without protection.

# Real-Life Use:
# Synchronized resource managers are useful for connection pools, shared caches, task lists, inventory systems, and other shared application resources.