"""
Coding Question 2: Find Biggest Book
------------------------------------
Use the Function Design Recipe to define a function called find_biggest_book. 

The function searches the Google Books database presented in the "PASS Mock Final" Word doc and
returns a tuple with the name of the largest book as the first index and 
the number of pages of the largest book as the second index.
"""
# This is just one possible solution!

# Why did I use a for loop instead of a while loop?
# Why did I set biggest_book_title to be an empty string?
# Why did I set biggest_book_pages to be -1?
# Is this code readable?
# How would you improve the code to make it more resilient?

def find_biggest_book(book_dict: dict) -> tuple:
    """
    Searches a Google Books database and
    returns the name and number of pages of the biggest book.
    """
    biggest_book_title = ""
    biggest_book_pages = -1

    for publisher in book_dict:
        for book in book_dict[publisher]:
            if book[pages] > biggest_book_pages:
                biggest_book_title = book[title]
                biggest_book_pages = book[pages]

    return (biggest_book_title, biggest_book_pages)
