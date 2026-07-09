# A Program to create a simple To-Do List.

tasks = []

print("\n")
while True:
    task = input("Enter a task (or 'done' to finish): ")

    if task.lower() == "done":
        break

    tasks.append(task)

print("\nYour Tasks:")

for task in tasks:
    print("-", task)

# Explanation:
# The program builds a simple task manager where users can add multiple tasks. Each task is stored inside a list and displayed at the end using a for loop. This challenge combines loops, lists, user input, and iteration to create a small but practical application similar to many productivity tools.