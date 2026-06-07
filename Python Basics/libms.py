# Self Challenge - Library Management System (OOP Version)

class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

class Members:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

class Library:
    def __init__(self):
        self.__books = []
        self.__members = []
    
    def add_book(self, book_id, title, author, availability):
        book = Book(
            book_id,
            title,
            author,
            availability
        )

        self.__books.append(book)
        print("Done. Book Added")
    
    def add_member(self, member_id, name):
        member = Members(
            member_id,
            name
        )

        self.__members.append(member)
        print("Done. Member Added")

    def display_books(self):
        print("BookID\tTitle\tAuthor\tAvailability\n")
        for i in range(len(self.__books)):
            print(f"{self.__books[i].book_id}\t{self.__books[i].title}\t{self.__books[i].author}\t{self.__books[i].availability}\n ")
    
    def display_members(self):
        print("MemberID\tName")
        for i in range(len(self.__members)):
            print(f"{self.__members[i].member_id}\t{self.__members[i].name}\n")
    
    def borrow_book(self, book_id):
        for i in range(len(self.__books)):
            if book_id == self.__books[i].book_id:
                self.__books[i].availability = False
                print("Book Borrowed")
                return
        print("Data not Found")

    def return_book(self, book_id):
        for i in range(len(self.__books)):
            if book_id == self.__books[i].book_id:
                self.__books[i].availability = True
                print("Book Returned")
                return
        print("Data not Found.")

# Main Function
library = Library()

print("Library Management System")
try:
    while True:
        option = int(input("Press 1 for Adding a Book\nPress 2 for registering a member\nPress 3 to Display all Books\nPress 4 to display all members\nPress 5 to borrow a book\nPress 6 for returning a book\nPress Ctrl+C for exit.\n>"))

        if option == 1:
            book_id = int(input("Enter the Book ID:"))
            title = input("Enter the Title:")
            author = input("Enter the author:")
            availability = True

            library.add_book(book_id, title, author, availability)


        elif option == 2:
            member_id = int(input("Enter the member ID:"))
            name = input("Enter the Member name")

            library.add_member(member_id, name)
        
        elif option == 3:
            library.display_books()

        elif option == 4:
            library.display_members()
        
        elif option == 5:
            book_id = int(input("Enter the Book ID:"))
            library.borrow_book(book_id)

        elif option == 6:
            book_id = int(input("Enter the Book ID:"))
            library.return_book(book_id)

except KeyboardInterrupt:
    print("Closing. Thank you.")

        


