"""
Author: Braeden Kloke
Version: March 19, 2022

Week: 4
Activity: 3

This Python code was designed for a "ECOR 1042: Data Management" PASS workshop.

Core concepts covered include:
* Dictionaries
* Nested Loops


Activity: Implementing a Bookshelf using a Dictionary
------------------------------------------------
Implement a bookshelf using a dictionary.

Implement the following functions:

* [X] empty_bookshelf: Returns an empty bookshelf with 3 shelves. The shelves are organized
by the following categores: Horror, Wizardy, and Recipes.

* [ ] set_king: Sets books by Stephen King onto the Horror shelf of a given bookshelf.

* [ ] set_rowling: Sets books by J.K. Rowling onto the Wizardry shelf of a given bookshelf.

* [ ] count_books: Returns the number of books on a given bookshelf.

* [ ] find_biggest_book: Returns the biggest book on a given bookshelf. The biggest book has the most number of pages.

"""
BOOKS_BY_KING = [
    {"title" : "Cujo", "page" : 309}, 
    {"title" : "IT", "page" : 1138}
]

BOOKS_BY_ROWLING = [
    {"title" : "The Philosopher's Stone", "page" : 223},
    {"title" : "Chamber of Secrets", "page" : 251},
    {"title" : "Goblet of Fire", "page" : 636}
]

def empty_bookshelf() -> dict:
    """
    Returns an empty bookshelf with 3 shelves. The shelves are organized by
    the following categories: Horror, Wizardry, and Recipes.

    >>> bookshelf = empty_bookshelf()
    >>> print(bookshelf)
    {'Horror': [None], 'Wizardry': [None], 'Recipes': [None]}
    """
    bookshelf = {
        "Horror" : [None],
        "Wizardry" : [None],
        "Recipes" : [None]
    }
    return bookshelf

def set_king(bookshelf: dict) -> None:
    """
    Sets books by Stephen King onto the Horror shelf of a given bookshelf.
    
    >>> bookshelf = empty_bookshelf()
    >>> set_king(bookshelf)
    >>> print(bookshelf)
    {'Horror': [{"title" : "Cujo", "page" : 309}, {"title" : "IT", "page" : 1138}], 
    'Wizardry': [None], 
    'Recipes': [None]}
    """
    # TODO Body
 
def set_rowling(bookshelf: dict) -> None:
    """
    Sets books by J.K. Rowling onto the Wizardry shelf of a given bookshelf.
    
    >>> bookshelf = empty_bookshelf()
    >>> set_king(bookshelf)
    >>> set_rowling(bookshelf)
    >>> print(bookshelf)
    {'Horror': [{"title" : "Cujo", "page" : 309}, {"title" : "IT", "page" : 1138}], 
    'Wizardry': [{"title" : "The Philosopher's Stone", "page" : 223}, {"title" : "Chamber of Secrets", "page" : 251}, {"title" : "Goblet of Fire", "page" : 636}], 
    'Recipes': [None]}
    """
    # TODO Body

def count_books(bookshelf: dict) -> int:
    """
    # TODO Description

    >>> bookshelf = empty_bookshelf()
    >>> count_books(bookshelf)
    0
    >>> set_king(bookshelf)
    >>> count_books(bookshelf)
    2
    >>> set_rowling(bookshelf)
    >>> count_books(bookshelf)
    5
    """
    count = 0

    # TODO Body

    return count

def find_biggest_book(bookshelf: dict) -> dict:
    """
    # TODO Description

    >>> TODO Examples
    """
    biggest_book = {}

    # TODO Body

    return biggest_book