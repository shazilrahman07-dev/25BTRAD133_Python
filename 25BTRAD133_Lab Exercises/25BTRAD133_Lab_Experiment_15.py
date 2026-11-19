
class Book:
    def __init__(self, name):
        self.name = name
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print("Book issued successfully!")
        else:
            print("Book is not available!")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfully!")
        else:
            print("Book was not issued!")

    def display(self):
        print(self.name, "-", "Available" if self.available else "Issued")


books = [Book("Python"), Book("Java"), Book("C++")]

while True:
    print("\n1. Display Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for book in books:
            book.display()

    elif choice == "2" or choice == "3":
        name = input("Enter book name: ")
        found = False

        for book in books:
            if book.name.lower() == name.lower():
                found = True
                if choice == "2":
                    book.issue()
                else:
                    book.return_book()
                break

        if not found:
            print("Book not found!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")
