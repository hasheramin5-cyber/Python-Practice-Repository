# A Program to display flight information.

flights = (
    ("PK301", "Lahore", "Karachi"),
    ("PK205", "Islamabad", "Dubai"),
    ("PK410", "Karachi", "Jeddah")
)

print("Flight Information\n")

for flight, source, destination in flights:
    print(f"{flight}: {source} → {destination}")

# Explanation:
# The program stores flight details inside nested tuples. Each record contains a flight number, departure city, and destination city. During each iteration, the tuple is unpacked into three variables and displayed. Organizing related information in tuples keeps the records structured and easy to process.