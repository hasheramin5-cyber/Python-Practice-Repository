# A Program to remove an attribute using a property deleter

class User:
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username

    @username.deleter
    def username(self):
        print("Removing username...")

        del self._username


user = User("alice123")

print("Username:", user.username)

del user.username

print("User data removed.")


# Explanation:
# The @property decorator provides access to the username attribute.
# The @username.deleter decorator defines the behavior that should occur when the property is deleted.
# The del statement triggers the deleter method.
# Inside the deleter, the internal _username attribute is removed using the del statement.
# This gives the class control over how an attribute is deleted instead of allowing uncontrolled deletion.

# Real-Life Use:
# Property deleters can be useful when removing resources, clearing stored data, closing connections, or resetting object state requires additional logic.