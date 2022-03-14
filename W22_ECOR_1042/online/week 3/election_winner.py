"""
ECOR 1042 Dictionary Problem

We’ve been tasked to write a function, election_winner, that accepts a 2D collection representing the votes in a
federal election and a city. The votes are formatted as a tuple containing tuples - each tuple contains the name of
a candidate in the first index, and the city in the second index.

An example of the input votes is provided at the end of this problem description
(suppose the appropriate constants have been defined.

The function we write needs to find and return the name of the winner of an election in a given city.
For example,

print(election_winner(votes, OTTAWA))

should print “mickey” (MICKEY)  since in Ottawa, the votes counts are:

jamie 2
mickey 3
tovald 1
obi 1

So “mickey” should win.
"""

# Constants

# Candidate Names
JAMIE = "jamie"
MICKEY = "mickey"
OBI = "obi"
TOVALD = "tovald"

# Cities
OTTAWA = "ottawa"
TORONTO = "toronto"
MONTREAL = "montreal"
SASKATOON = "saskatoon"


def election_winner():
    """
        Don't forget to add examples, parameters, type annotations,
        and a description!
        >>>
        >>>
    """
    pass


votes = (
    (JAMIE, OTTAWA),
    (JAMIE, TORONTO),
    (OBI, SASKATOON),
    (TOVALD, TORONTO),
    (MICKEY, OTTAWA),
    (MICKEY, OTTAWA),
    (MICKEY, MONTREAL),
    (TOVALD, OTTAWA),
    (OBI, OTTAWA),
    (JAMIE, SASKATOON),
    (MICKEY, SASKATOON),
    (JAMIE, SASKATOON),
    (OBI, SASKATOON),
    (TOVALD, MONTREAL),
    (MICKEY, OTTAWA),
    (JAMIE, OTTAWA),
    (TOVALD, SASKATOON),
    (OBI, TORONTO),
    (JAMIE, TORONTO),
    (TOVALD, TORONTO),
    (MICKEY, TORONTO)
)
