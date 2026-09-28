# A Program to create pages from a collection using a generator

def paginate(items, page_size):
    for start in range(0, len(items), page_size):
        yield items[start:start + page_size]


products = [
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Headphones",
    "Webcam",
    "Microphone",
    "Speaker"
]

pages = paginate(products, 3)

for page_number, page in enumerate(pages, start=1):
    print("Page:", page_number)
    print(page)


# Explanation:
# The paginate() generator divides a collection into smaller pages.
# The page_size parameter determines how many items each page can contain.
# Each slice is returned using yield.
# enumerate() is then used to assign a page number to every generated page.
# The generator allows each page to be processed separately instead of manually creating all pages first.

# Real-Life Use:
# Pagination is commonly used when displaying products, users, search results, database records, and API responses.