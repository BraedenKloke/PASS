"""
    One possible solution among many. Make sure you 
    understand why each line is needed - once you do, I 
    recommend trying to write your own solution from memory/intuition.
"""

def alpha_count() -> None:
    """
        Prompts the user to enter single letters of the alphabet until
        they enter 0 to stop. Once they stop, prints out the most
        frequently input letter along with a percentage of how frequently it
        was input.

        Characters other than a letter or 0 result in a warning to the user.
    """

    # String of valid characters - anything not in here is not valid.
    valids = 'abcdefghijklmnopqrstuvwxyz0'

    # The last input from the user
    character_input = ''

    # A dictionary to keep count of the valid inputs
    """
    An example for inputs: a, a, b, c, a, c
    { 'a': 3, 'b': 1, 'c': 2}
    """
    dictionary_count = {}

    # Keep asking the user for letters until they enter 0
    while character_input != '0':
        # Get the input
        character_input = input("Please input a single letter (0 to quit):")
        character_input = character_input.lower()   # Make it lowercase to simplify things 

        # Make sure it's a single character
        if len(character_input) > 1:
            print("This is not a single character")

        # Make sure it's valid (a letter or 0 - no special characters or punctuation)
        elif character_input not in valids:
            print("Not a valid character")

        # If it's 0, don't count it and let the user know they quit
        elif character_input == '0':
            print("Quitting. Bye!")

        # If everything above is false, we have a letter.
        else:
            dictionary_count[character_input] = dictionary_count.get(character_input, 0) + 1

    # Get the most frequently input character and its percentage
    # We'll loop over the entire dictionary and...

    # Store the most frequently input character that we've seen so far.
    most_frequent_so_far = ''

    # Store the amount of time this most frequently input character
    # so far has been input -> anything input more times will be the new most frequently input
    most_frequent_count_so_far = 0

    # Keep track of the total count of inputs to get a percentage
    total_count = 0

    # Loop through all characters
    for character in dictionary_count:
        # Get the character's count
        count = dictionary_count[character]
        # And update the total count
        total_count += count

        # Check if this character was input more times that the
        # most frequently input character we've seen so far - if so
        # this is the new most frequent
        if count > most_frequent_count_so_far:
            most_frequent_count_so_far = count
            most_frequent_so_far = character

    # Once we've looped over all the characters - we have the true most frequently input and can get it's percentage
    print("Most frequent letter:", most_frequent_so_far, ". Percentage:", most_frequent_count_so_far * 100 / total_count, "%")
        
# Test
alpha_count()