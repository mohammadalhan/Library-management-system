import csv
class Book:
    genre_names = {
        0: "Romance",
        1: "Mystery",
        2: "Science Fiction",
        3: "Thriller",
        4: "Young Adult",
        5: "Children's Fiction",
        6: "Self-help",
        7: "Fantasy",
        8: "Historical Fiction",
        9: "Poetry"
    }
    
    def __init__(self, isbn, title, author, genre_code, available):
        """This is the intializer of Book class which contains 5 attributes."""
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre_code = genre_code
        self.available = available
    
    def get_genre_name(self):
        """Getter method to retrieve genre name"""
        return self.genre_names.get(self.genre_code, "Unknown Genre")

    def get_isbn(self):
        """getter method to get the isbn number of the book."""
        return self.isbn

    def get_title(self):
        """getter method to get the title of the book."""
        return self.title

    def get_author(self):
        """getter method to get the name of the author"""
        return self.author

    def get_genre_code(self):
        """getter method to get the genre_code"""
        return self.genre_code

    def get_availability(self):
        """to get the availability of the book"""
        return "Available" if self.available else "Borrowed"

    def borrow_it(self):
        """Set the availability to False when book is borrowed"""
        self.available = False

    def return_it(self):
        """Set the availabilty to True when book is returned."""
        self.available = True

    def __str__(self):
        """String method to display all the attributes."""
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Genre Code: {self.genre_code}, Available: {self.available}"

    
def load_books(book_list, csv_path):
    """Takes the csv file path and load in the terminal."""
    books_loading = True
    while books_loading:
        try:
            with open(csv_path, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  
                loaded_books = 0  
                for row in csv_reader:
                    if len(row) == 5:  
                        isbn, title, author, genre, available = row
                        genre = int(genre) 
                        available = available.lower() == 'true' 
                        book_list.append(Book(isbn, title, author, genre, available))
                        loaded_books += 1                     
            print("Book catalog has been loaded.")
            return loaded_books  
        except FileNotFoundError:
            csv_path = input("File not found. Re-enter the path to the CSV data file: ")
            continue
        except Exception as e:
            print(f"Error occurred while loading books: {e}")
            return 0