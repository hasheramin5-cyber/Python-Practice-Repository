# A Program to use Tuples as Dictionary keys.

locations = {
    (31.5204, 74.3587): "Lahore",
    (24.8607, 67.0011): "Karachi"
}

coordinate = (31.5204, 74.3587)

print("Location:", locations[coordinate])

# Explanation:
# The program uses tuples as dictionary keys. Since tuples are immutable, Python allows them to be used as keys, unlike lists. Each tuple represents a pair of GPS coordinates, and the dictionary stores the corresponding city name as the value. This technique is commonly used in mapping systems, geographic applications, and data lookup tables where fixed values uniquely identify information.