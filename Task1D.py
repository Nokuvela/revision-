import pandas as pd 
books_df = pd.DataFrame(columns=["book_id","title","author","status"])

members_df=pd.DataFrame(columns=["member_id","name","borrowed_book"])

new_book = pd.DataFrame({"book_id": [2024001], "title": ["Python Programming"], "author": ["Jacob Zuma"], "status": ["available"]})
books_df=pd.concat([new_book,books_df],ignore_index=True)

new_member = pd.DataFrame({"member_id": [1], "name": ["Anelisa Maleka"], "borrowed_books": [[]]})

members_df=pd.concat([new_member,members_df],ignore_index=True)


print("book df")

print(books_df)

print("member_df")
print(members_df)

