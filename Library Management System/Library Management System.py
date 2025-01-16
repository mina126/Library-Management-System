from operator import index


class Book:
    def __init__(self, title, author, status="available"):
        self.tite = title
        self.author = author
        self.status = status

    def borrow(self):
        if self.status == "available":
            self.status = "borrowed"
            print(f"he is borrowed {self.tite}")
        else:
            print(f"He is not avaiable {self.tite}")

    def return_book(self):
        if self.status == "borrowed":
            self.status = "available"
            print(f"he is available {self.tite}")
        else:
            print(f"He is not borrowed {self.tite}")

    def __str__(self):
        return f"{self.tite} - {self.status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(" He is append")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(" He is remove")
        else:
            print("He is not her ")

    def search_book(self,tite):
        for book in self.books:
            if book.tite == tite:
                print(f"Book found: {book.tite} by {book.author}")
                return
        print("Book not found.")

    def show_available_books(self):
        # عرض الكتب المتاحة فقط
        available_books = [book for book in self.books if book.status == "available"]
        if available_books:
            for book in available_books:
                print(
                    f"Title: {book.tite}, Author: {book.author}, Status: {book.status}"
                )
        else:
            print("No available books in the library.")

    def borrow_book(self, tite):
        for book in self.books:
            if book.tite == tite and book.status == "available":
                book.status = "borrowed"
                print(f"You have borrowed: {book}")
                return
        print(f"Sorry, the book '{tite}' is either not available or already borrowed.")

    def return_book(self, tite):
        for book in self.books:
            if book.tite == tite and book.status == "borrowed":
                book.status = "available"
                print(f"You have returned: {book}")
                return
        print(f"Sorry, the book '{tite}' is either not borrowed or does not exist.")

    def show_available_books(self):
        available_books = [book for book in self.books if book.status == "available"]
        if available_books:
            for book in available_books:
                print(book)




if __name__ == "__main__":
    book1 = Book("Python Programming", "John Doe")
    book2 = Book("Data Structures", "Jane Smith")
    book3 = Book("Machine Learning", "Alan Turing")

   
    library = Library()

   
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)


    library.search_book("Python Prog
    # library.borrow_book("Data Structures")


    # library.borrow_book("Python Programming")


    # library.return_book("Python Programming")


    # print("\nAvailable Books After Returning 'Python Programming':")
    # library.show_available_books()
