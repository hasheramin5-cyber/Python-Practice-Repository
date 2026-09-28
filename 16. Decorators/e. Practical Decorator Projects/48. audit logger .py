# A Program to create an audit logger using a decorator

from functools import wraps
from datetime import datetime


def audit(function):
    @wraps(function)
    def wrapper(username, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(
            f"[{timestamp}] "
            f"User: {username} | "
            f"Action: {action}"
        )

        return function(username, action)

    return wrapper


@audit
def update_profile(username, action):
    print(f"{username} performed: {action}")


update_profile("Hasher", "Updated profile picture")
update_profile("Amin", "Changed username")


# Explanation:
# The audit() decorator records information about important user actions before the original function executes.
# datetime.now() generates the current local date and time.
# The wrapper combines the timestamp, username, and action into an audit message.
# The original function then performs the requested operation.
# The decorator allows auditing behavior to be added without placing logging code inside every individual function.

# Real-Life Use:
# Audit logging is useful for administrative systems, account activity tracking, business applications, and operations where user actions need to be recorded.