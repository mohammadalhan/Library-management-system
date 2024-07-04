def print_books(book_list):
    """Method to print the whole data of the csv file in the terminal after entering option 6."""
    print("Print book catalog")
    print("ISBN".ljust(15), "Title".ljust(25), "Author".ljust(25), "Genre".ljust(20), "Availability".ljust(15))
    print("-" * 15, "-" * 25, "-" * 25, "-" * 20, "-" * 15)
    for books in book_list:
        genre_name = Book.genre_names.get(books.get_genre_code(), "Unknown Genre")
        print(books.isbn.ljust(15), books.title.ljust(25), books.author.ljust(25), genre_name.ljust(20), books.get_availability().ljust(15))

def print_menu(menu_heading, menu_options):
    """This method print out the whole menu after entering the csv file in load_books() method."""
    print(menu_heading)
    print("=" * len(menu_heading))
    for key, value in menu_options.items():
        print(f"{key}: {value}")

    while True:
        user_input = input("Enter your selection: ")
        if user_input in menu_options:
            return user_input
        if user_input == '2130':
            return user_input
        else :
            print("invalid option.") 
            if user_input in menu_options: 
                return user_input
            
              
def search_books(book_list, search_string):
    """method gives the detail of the book after entering any information about the book."""
    search_result = []
    for book in book_list:
        if (search_string.lower() in book.get_isbn().lower() 
            or search_string.lower() in book.get_title().lower() 
            or search_string.lower() in book.get_author().lower() 
            or search_string.lower() in book.get_genre_name().lower()): 
            search_result.append(book)
    return search_result