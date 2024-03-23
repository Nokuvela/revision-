books = []
members = []

def add_book():
    books.append({
        "book_id": 2024001,
        "title": "Python Programming",
        "author": "Jacob Zuma",
        "status": "Available"
    })

def add_member():
    members.append({
        "member_id": 1,
        "name": "Nelisa",
        "borrowed_books": []
    })

# Call the functions to add books and members
add_book()
add_member()

# Print the lists
print("Book list:")
print(books)

print("Member list:")
print(members)
