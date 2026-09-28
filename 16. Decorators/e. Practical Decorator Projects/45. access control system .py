# A Program to build a simple role-based access control system

from functools import wraps


def require_role(required_role):
    def decorator(function):
        @wraps(function)
        def wrapper(username, role):
            if role != required_role:
                print(
                    f"Access denied for {username}. "
                    f"Required role: {required_role}"
                )

                return

            return function(username, role)

        return wrapper

    return decorator


@require_role("admin")
def delete_user(username, role):
    print(f"{username} deleted a user.")


delete_user("Alice", "admin")
delete_user("Bob", "user")


# Explanation:
# require_role() is a decorator factory that receives the role required to execute a function.
# The wrapper checks the role supplied by the caller.
# If the role does not match the required role, execution stops and an access-denied message is displayed.
# If the role is correct, the original function is executed.
# This keeps authorization logic separate from the operation being protected.

# Real-Life Use:
# Role-based decorators are useful for administrative actions, protected features, dashboards, and application authorization.
# Real security systems should use proper authentication, authorization, sessions, and secure identity management.