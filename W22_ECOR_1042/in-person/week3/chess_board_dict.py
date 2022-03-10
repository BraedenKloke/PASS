"""
Author: Braeden Kloke
Version: March 10, 2022

Week: 3
Activity: 3.2

This Python code was designed for a "ECOR 1042: Data Management" PASS workshop.

Core concepts covered include:
* Incremental Development
* Dictionaries


Activity: Implementing a Chess Board using a Dictionary
------------------------------------------------
Implement a chess board using a dictionary.

Requirements:

* The red pieces must be on the 'North' side and
the black pieces must be on the 'South' side

* The positions of pieces must be stored as a list of tuples.


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


def empty_board() -> dict:
    """Returns an 8 x 8 empty chess board."""
    board = {
        (RED, KING): [None], (BLACK, KING): [None],
        (RED, ROOK): [None], (BLACK, ROOK): [None],
        (RED, PAWN): [None], (BLACK, PAWN): [None]
    }

    return board


def set_kings(board: dict) -> None:
    """
    TODO description
    
    >>> board = empty_board()
    >>> set_kings(board)
    >>> board.get((RED, KING))
    [(0,3)]
    >>> set_kings(board)
    >>> board.get((BLACK, KING))
    [(7,4)]
    
    """
    # TODO body


def set_rooks(board: dict) -> None:
    """
    TODO description
    
    >>> TODO examples
    """
    # TODO body


def set_pawns(board: dict) -> None:
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
