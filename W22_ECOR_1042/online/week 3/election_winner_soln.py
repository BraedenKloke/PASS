# type: ignore
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

    # For each vote (tuple) in all our votes
    for vote_tuple in votes:
        candidate, vote_city = vote_tuple

        # Filter for the votes in our city of interest
        if vote_city == city:
            vote_dict[candidate] = vote_dict.get(candidate, 0) + 1

    """
        Will eventually look like:
        vote_dict = {
            "jamie": 2,
            "mickey": 3,
            "obi": 1,
            "tovald": 1
        }

        Let's find the winner (mickey)
    """

    # We'll need to go through each candidate to find the winner.
    # So, let's keep track of the best one we've seen as we loop

    winner_so_far = ""  # The winning candidate we've seen so far (while looping)
    winner_votes = -1   # The winner's votes, if we see someone with more votes that
                        # this, then they're the new winner. We initialize this
                        # to -1 so that the first person we see becomes the best winner so far (since they have >= 1 votes).

    # Loop through all candidates and their votes
    for candidate, num_votes in vote_dict.items():
        # If we see a candidate better than the one
        # we have so far - update our winner (so far).
        if num_votes > winner_votes:
            winner_votes = num_votes
            winner_so_far = candidate

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

print(election_winner(votes, OTTAWA))           # mickey
print(election_winner(votes, MONTREAL))         # mickey
print(election_winner(votes, SASKATOON))        # obi
print(election_winner(votes, TORONTO))          # jamie
