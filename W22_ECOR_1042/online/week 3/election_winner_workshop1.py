# Constants
from typing import Any

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


def election_winner(votes: Any, city: str) -> str:
    """
        Don't forget to add examples, parameters, type annotations,
        and a description!
        >>>
        >>>
    """

    """
    vote_dict = {
    }
    """
    vote_dict = {}

    # Loop over all the votes, and print the candidate and the city
    for candidate, candidate_city in votes:
        # Only print the votes in the specified city (from our parameter)
        if candidate_city == city:
            # Count the votes for each candidate in the city
            print(candidate, candidate_city)

            # if candidate not in vote_dict.keys():
            #     vote_dict[candidate] = 0
            # vote_dict[candidate] =  vote_dict[candidate] + 1       # current_num_votes + 1 number of votes candidate has

            vote_dict[candidate] = vote_dict.get(candidate, 0) + 1

            print(vote_dict)

    return ""


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

election_winner(votes, OTTAWA)

"""
print(election_winner(votes, OTTAWA))
print(election_winner(votes, MONTREAL))
print(election_winner(votes, SASKATOON))
print(election_winner(votes, TORONTO))
"""
