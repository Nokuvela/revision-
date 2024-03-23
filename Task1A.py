


books = []
members = []

def add_book(book_id,title,author,status):
   books.append({
     "book_id":book_id,
     "title":title,
     "author":author,
     "status":status
   })
def add_member(member_id, name,borrowed_member):
    members.append({
        "member_id":member_id,
        "name":name,
        "borrowed_member":[]
    })

    add_book( 2024001 ,"Python Programming", " Jacob Zuma" , "Available")

    add_member(1,"Nelisa","Maleka")

    print("book_list")
    print(books)

    print("member list")
    print(members)
    