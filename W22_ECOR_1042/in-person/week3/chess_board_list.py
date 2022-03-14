"""
Author: Braeden Kloke
Version: March 10, 2022

Week: 3
Activity: 3.1

This Python code was designed for a "ECOR 1042: Data Management" PASS workshop.

Core concepts covered include:
* Incremental Development
* 2D Matrices


Activity: Implementing a Chess Board using Lists
------------------------------------------------
Implement a chess board using 2D lists.

Requirements:

* The red pieces must be on the 'North' side and
the black pieces must be on the 'South' side

* A piece's colour and rank must be stored as a tuple with two elements.
For example, a red pawn would be stored as ("R", "P").


Implement the following functions:

* [X] empty_board: Returns an 8 x 8 empty chess board.

* [ ] set_kings: Sets both teams' kings to their starting positions on the chess board.

* [ ] set_rooks: Sets both teams' rooks to their starting positions on the chess board.

* [ ] set_pawns: Sets both teams' pawns to their starting positions on the chess board.

* [ ] get_position: Returns the coordinate position of a given piece.

"""
RED = "R"
BLACK = "B"
KING = "K"
ROOK = "R"
PAWN = "P"


def empty_board() -> list:
    """Returns an 8 x 8 empty chess board."""
    board = [[None] * 8 for i in range(8)]

    return board


def set_kings(board: list) -> None:
    """
    TODO description
    
    >>> board = empty_board()
    >>> set_kings(board)
    >>> board[0][3]
    ('red', 'king')
    >>> board[7][4]
    ('black', 'king')
    """
    # TODO body


def set_rooks(board: list) -> None:
    """
    TODO description
    
    >>> TODO examples
    """
    # TODO body


def set_pawns(board: list) -> None:
    """
    TODO
    
    >>> TODO
    """
    # TODO


def get_position(colour: str, rank: str) -> tuple:
    """
    TODO
    
    >>> board = empty_board()
    >>> set_kings(board)
    >>> get_position(RED, KING)
    (0,3)
    >>> get_position(RED, QUEEN)
    None
    """
    # TODO




