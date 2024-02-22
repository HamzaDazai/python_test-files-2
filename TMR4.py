# TMR4
print("Welcome sir")
list_book_have = []
book_have = input("Enter the name a book you own: ").lower()
list_book_have.append(book_have)
book_have2 = input("\nEnter the name of another book you own (or press enter to  skip this): ").lower()
if book_have2:
    list_book_have.append(book_have2)
    print(f"Your library {list_book_have}")
else:
    print(f"Your library {list_book_have}")

list_book_wish = []
book_wish = input("\nEnter the name of book you wish to have in the future: ").lower()
list_book_wish.append(book_wish)
book_wish2 = input("Enter the name of another bo you wish to have in the future (or press enter to skip this): ").lower()
if book_wish2:
    list_book_wish.append(book_wish2)
    print(f"Your Wishlist {list_book_wish}")
else:
    print(f"Your Wishlist {list_book_wish}")

book_hw = input("Enter the name of a book from your wishlist that you've buy (or press 'Enter' to skip): ").lower()
if book_hw:
    list_book_have.append(book_hw)
    list_book_wish.remove(book_hw)
    print(f"Updated your library own {list_book_have}")
    print(f"Updated Wishlist: {list_book_wish}")
else:
    print(f"Your wishlist {list_book_wish}")
    print(f"Your library {list_book_have}")

book_donted = input("Enter the name of the book you donted from library (or press 'Enter' to skip): ").lower()
if book_donted:
    list_book_have.remove(book_donted)
    list_finale = (list_book_have + list_book_wish)
    print(f"Final Library after Donations: {list_finale}")
else:
    list_finale = (list_book_have + list_book_wish)
    print(f"The final Library : {list_finale}")