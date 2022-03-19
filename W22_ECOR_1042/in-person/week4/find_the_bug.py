"""
Author: Braeden Kloke
Version: March 19, 2022

Week: 4
Activity: 2

This Python code was designed for a "ECOR 1042: Data Management" PASS workshop.

Core concepts covered include:
* Nested Loops
* Dictionaries


Activity: Find the Bug!
-----------------------

Some of the code will run. Some of it won't. It's up to the student to find the bugs!
"""
# Q1

# {category}
bookshelf_set = {
    "Horror", 
    "Wizardry", 
    "Recipes"
}

def print_categories1(bookshelf: set) -> None:
    """
    Prints the categories on a bookshelf.

    >>> print_categories1(bookshelf_set)
    Horror
    Wizardy
    Recipes
    """
    for category in bookshelf:
        print(category)


# Q2

# {category : book_title}
bookshelf_dict1 = {
    "Horror" : "Cujo", 
    "Wizardry" : "The Philosopher's Stone", 
    "Recipes" : "Spam"
}

def print_categories2(bookshelf: dict) -> None:
    """
    Prints the categories on a bookshelf.

    >>> print_categories2(bookshelf_dict1)
    Horror
    Wizardy
    Recipes
    """
    for category in bookshelf:
        print(category)


# Q3

# {category : book_title}
bookshelf_dict2 = {
    "Horror" : "Cujo", 
    "Wizardry" : "The Philosopher's Stone", 
    "Recipes" : "Spam"
}

def print_books1(bookshelf: dict) -> None:
    """
    Prints the books on a bookshelf.

    >>> print_books1(bookshelf_dict2)
    Cujo
    The Philospher's Stone
    Spam
    """
    for category in bookshelf:
        for book in category:
            print(book)


# Q4

# {category : [book_title]}
bookshelf_dict3 = {
    "Horror" : ["Cujo", "IT"], 
    "Wizardry" : ["The Philosopher's Stone"], 
    "Recipes" : ["Spam", "Ham", "Bacon", "Spam"]
}

def print_books2(bookshelf: dict) -> None:
    """
    Prints the books on a bookshelf.

    >>> print_books2(bookshelf_dict3)
    Cujo
    IT
    The Philospher's Stone
    Spam
    Ham
    Bacon
    Spam
    """
    for category in bookshelf:
        for book in category:
            print(book)


# Q5

# {category : [(book_title, num_pages)]}
bookshelf_dict4 = {
    "Horror" : [("Cujo", 309), ("IT", 1138)], 
    "Wizardry" : [("The Philosopher's Stone", 223)], 
    "Recipes" : [("Spam", 1), ("Ham", 1), ("Bacon", 1), ("Spam", 1)]
}

def print_books3(bookshelf: dict) -> None:
    """
    Prints the books on a bookshelf.

    >>> print_books3(bookshelf_dict4)
    Cujo
    IT
    The Philospher's Stone
    Spam
    Ham
    Bacon
    Spam
    """
    for category in bookshelf:
        for book in bookshelf:
            print(book)


# Q6

# {category : [(book_title, num_pages)]}
bookshelf_dict5 = {
    "Horror" : [
        ("Cujo", 309), 
        ("IT", 1138)
        ], 
    "Wizardy" : [
        ("The Philosopher's Stone", 223)
        ], 
    "Recipes" : [
        ("Spam", 1), 
        ("Ham", 1), 
        ("Bacon", 1), 
        ("Spam", 1)
        ]
}

def print_recipes1(bookshelf: dict) -> None:
    """
    Prints the recipes on a bookshelf.

    >>> print_recipes1(bookshelf_dict5)
    Spam
    Ham
    Bacon
    Spam
    """
    for category in bookshelf:
        for recipe in bookshelf.get(category):
            print(recipe[0])


# Q7

# {category : [{"title" : book_title, "page" : num_pages}]}
bookshelf_dict6 = {
    "Horror" : [
        {"title" : "Cujo", "page" : 309}, 
        {"title" : "IT", "page" : 1138}
        ], 
    "Wizardy" : [
        {"title" : "The Philosopher's Stone", "page" : 223}
        ], 
    "Recipes" : [
        {"title" : "Spam", "page" : 1}, 
        {"title" : "Ham", "page" : 1}, 
        {"title" : "Bacon", "page" : 1}, 
        {"title" : "Spam", "page" : 1}
        ]
}

def print_recipes2(bookshelf: dict) -> None:
    """
    Prints the recipes on a bookshelf.

    >>> print_recipes2(bookshelf_dict6)
    Spam
    Ham
    Bacon
    Spam
    """
    for category in bookshelf:
        for recipe in bookshelf.get(category):
            print(recipe[0])

