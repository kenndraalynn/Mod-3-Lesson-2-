
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library):
    while True:
        newbook = input("Please enter a book title and the author to add to the library (or type 'stop' to view library): ")
        if newbook.lower() == 'stop':
            break
        try:
            title, author = newbook.split(", ")
            library.append((title, author))
            print(f"Added '{title}' by {author} to the library.")
        except ValueError:
            print("Please enter the book title and author in the format 'Title, Author'.")

add_book(library)

print("Current Library:")
for book in library:
    print(f"Title: {book[0]}, Author: {book[1]}")