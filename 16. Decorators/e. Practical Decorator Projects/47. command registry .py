# A Program to create a command system using a decorator

commands = {}


def command(name):
    def decorator(function):
        commands[name] = function

        return function

    return decorator


@command("start")
def start():
    print("Application started.")


@command("stop")
def stop():
    print("Application stopped.")


@command("status")
def status():
    print("Application is running.")


user_command = "status"

if user_command in commands:
    commands[user_command]()
else:
    print("Unknown command.")


# Explanation:
# The commands dictionary stores functions using command names.
# The command() decorator factory receives the name that should be associated with each function.
# When a decorated function is defined, it is automatically added to the commands dictionary.
# The program can then look up a function using a command name.
# Instead of writing separate if statements for every command, the registry provides a centralized lookup system.

# Real-Life Use:
# Command registries are useful for CLI applications, plugin systems, automation tools, event handlers, and command-based software.