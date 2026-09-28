# A Program to check user permissions using a decorator

from functools import wraps


def require_permission(required_permission):
    def decorator(function):
        @wraps(function)
        def wrapper(username, permissions):
            if required_permission not in permissions:
                print(
                    f"Access denied for {username}. "
                    f"Required: {required_permission}"
                )

                return

            return function(username, permissions)

        return wrapper

    return decorator


@require_permission("delete")
def delete_file(username, permissions):
    print(f"{username} deleted the file.")


delete_file("Alice", ["read", "write", "delete"])
delete_file("Bob", ["read"])

# Explanation:
# require_permission() receives the permission required by the decorated function.
# The wrapper receives the username and the user's permissions.
# It checks whether the required permission exists inside the permissions list.
# If the permission is missing, the original function is not executed.
# If the permission exists, the original function runs normally.
# This separates permission-checking logic from the actual operation being protected.

# Real-Life Use:
# Permission decorators are useful for role-based access systems, administrative actions, protected application features, and API authorization patterns.