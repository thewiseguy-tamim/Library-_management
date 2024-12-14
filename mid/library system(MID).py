class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print("Book borrowed successfully.")
        else:
            raise Exception("This book is already borrowed.")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print("Book returned successfully.")
        else:
            raise Exception("This book is not borrowed.")

    def view_book_info(self):
        availability_status = "Available" if self.__availability else "Not Available"
        print(f"Book ID: {self.__book_id}\nTitle: {self.__title}\n Author: {self.__author}\nAvailability: {availability_status}")

    def get_book_id(self):
        return self.__book_id


def view_all_books():
    if not Library.book_list:
        print("No books available.")
        return

    for book in Library.book_list:
        book.view_book_info()
        


def borrow_book_by_id(book_id):
    for book in Library.book_list:
        if book.get_book_id() == book_id:
            try:
                book.borrow_book()
            except Exception as e:
                print(e)
            return
    print("Invalid book ID.")


def return_book_by_id(book_id):
    for book in Library.book_list:
        if book.get_book_id() == book_id:
            try:
                book.return_book()
            except Exception as e:
                print(e)
            return
    print("Invalid book ID.")

def main_menu():
    while True:
        print("\nMenu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                view_all_books()
            elif choice == 2:
                book_id = input("Enter the Book ID to borrow: ")
                borrow_book_by_id(book_id)
            elif choice == 3:
                book_id = input("Enter the Book ID to return: ")
                return_book_by_id(book_id)
            elif choice == 4:
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    Book("1", "University Bhalo Na", "Tamim Islam")
    Book("2", "1984", "George Orwell")
    Book("3", "The Art of Thinking Clearly", " Rolf Dobelli")

    main_menu()
