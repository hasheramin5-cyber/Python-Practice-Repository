# Convert seconds into hours, minutes, and seconds in Python.

seconds = int(input("Enter seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print(f"{hours} hour(s), {minutes} minute(s), {remaining_seconds} second(s)")

# Explaination:
# In this code snippet, we take the number of seconds as input from the user and convert it into hours, minutes, and remaining seconds. We use integer division (//) to calculate the number of hours and minutes, and the modulus operator (%) to find the remaining seconds. Finally, we print the result in a formatted string showing the hours, minutes, and seconds.