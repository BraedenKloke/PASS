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


def election_winner(votes: tuple[tuple[str, str], ...], city: str) -> str:
    """
        Don't forget to add examples, parameters, type annotations,
        and a description!
        >>>
        >>>
    """

    vote_dict = {}

    # Add the candidate
    for vote_tuple in votes:
        candidate, vote_city = vote_tuple

        if vote_city == city:
            vote_dict[candidate] = vote_dict.get(candidate, 0) + 1

    print(vote_dict)

    """
    vote_dict = {
        'jamie': 2, 
        'mickey': 3, 
        'tovald': 1, 
        'obi': 1
    }
    """

    winner_so_far = ""

    return winner_so_far


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

print(election_winner(votes, OTTAWA))
print(election_winner(votes, MONTREAL))
print(election_winner(votes, SASKATOON))
print(election_winner(votes, TORONTO))
