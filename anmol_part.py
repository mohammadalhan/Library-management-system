def borrow_book(book_list):
    """method to regulate the program if someone borrowed the book from the library."""
    isbn = input("Enter the 13-Digit ISBN (format 999-9999999999): ")
    book_available = next((book for book in book_list if book.get_isbn().lower() == isbn.lower()), None)
    if book_available:
        if book_available.get_availability() == "Available":
            book_available.borrow_it()
            print(f"'{book_available.get_title()}' with ISBN {isbn} succesfully borrowed.")
        else:
            print(f"'{book_available.get_title()}' with ISBN {isbn} is not currently available.")
    else:
        print("No book found with that ISBN.")

def return_book(book_list):
    """method to regulate the program if someone returned the book to the library."""
    isbn = input("Enter the 13-Digit ISBN (format 999-9999999999): ")
    book = next((book for book in book_list if book.get_isbn().lower() == isbn.lower()), None)
    if book:
        if book.get_availability() == "Borrowed":
            book.return_it()
            print(f"'{book.get_title()}' with ISBN {isbn} successfully returned.")
        else:
            print(f"'{book.get_title()}' with ISBN {isbn} is not currently borrowed.")
    else:
        print("No book found with that ISBN.")

def add_book(book_list):
    """method to add new books in the libarary data."""
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    genre_valid = False
    while not genre_valid:
        genre_name = input("Enter genre: ").title()
        genre_code = next((code for code, name in Book.genre_names.items() if name.lower() == genre_name.lower()), None)
        if genre_code is not None:
            genre_valid = True
        else:
            print(f"Invalid genre name. Valid genre choices are: {', '.join(Book.genre_names.values())}")
        
    new_book = Book(isbn, title, author, genre_code, True)
    book_list.append(Book(isbn, title, author, genre_code, True))
    with open( 'books.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([new_book.isbn, new_book.title, new_book.author, new_book.genre_code, new_book.available])  
    print(f"'{title}' with ISBN {isbn} successfully added.")