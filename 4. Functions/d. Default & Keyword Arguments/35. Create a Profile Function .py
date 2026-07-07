# A Program to create a user profile using keyword arguments.

def profile(name, city, profession):
    print("Name:", name)
    print("City:", city)
    print("Profession:", profession)

profile(
    profession="Student",
    city="Lahore",
    name="Hasher"
)

# Explanation:
# The program creates a simple user profile using keyword arguments. Since each argument is identified by its parameter name, the order of the arguments does not matter. This improves the readability of the function call.