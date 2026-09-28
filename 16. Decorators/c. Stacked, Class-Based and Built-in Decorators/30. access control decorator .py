# A Program to control function access using a decorator

from functools import wraps


def require_admin(function):
    @wraps(function)
    def wrapper(username, is_admin):
        if not is_admin:
            print(f"Access denied for {username}.")
            return

        return function(username, is_admin)

    return wrapper


@require_admin
def delete_account(username, is_admin):
    print(f"Account deleted by {username}.")


delete_account("Alice", True)
delete_account("Bob", False)


# Explanation:
# The require_admin() decorator adds an access-control check before the delete_account() function can execute.
# The wrapper receives the username and admin status.
# If is_admin is False, the decorator stops the original function from running and displays an access-denied message.
# If is_admin is True, the original function is executed.
# The decorator therefore separates access-control logic from the main delete_account() function.
# In real applications, authentication and authorization systems would normally use stronger security mechanisms than this simple example.

# Real-Life Use:
# Access-control decorators can be used as a simple pattern for protecting administrative operations, restricted actions, API endpoints, and application features.