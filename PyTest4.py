#main class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False 
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You returned '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' was not borrowed.")
#books
books = [
    Book("Life of Fred", "Polka dot publising"),
    Book("To Kill a Mockingbird", "Harper Lee"),
    Book("The Great Gatsby", "F. Scott Fitzgerald")
]
'''
# borrow system old
book1.borrow()
book1.return_book()
book2.borrow()
book2.borrow()       # shows already borrowed
book2.return_book()
book3.borrow()
book3.return_book()'''

#borrow system new
while True: 
    print("\nLibrary Menu")
    for i,book in enumerate(books, start=1):
        status = "Available" if not book.is_borrowed else "Borrowed"
        print(f"{i}. {book.title} by {book.author} ({status})")
    choice = input("\nChoose a book number or q to quit: ")
    if choice.lower() == 'q':
        print("Thank's for using codingal library")
        break
    if choice.isdigit() and 1 <= int(choice) <= len(books):
        book = books[int(choice) - 1]
        action = input("Type b to borrow or r to return: ").lower()
        if action == 'b':
            book.borrow()
        elif action == 'r':
            book.return_book()
        else:
            print("Invalid action, please try again.")
    else:
        print("Invalid action, please try again.")
