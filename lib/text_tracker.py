# 1. Describe the Problem
# Put or write the user story here. Add any clarifying notes you might have.

# User story: check to see if a specific string is an a given text

# 2. Design the Function Signature
# Include the name of the function, its parameters, return value, and side effects.

def find_special_string_in_text(text,special_string):
    # Parameters:
    # takes two param ,both strings
    # one represents special string ,the other represents the text in which the special string is
    # Returned value:
    # returns True if special string exists ,returns False otherwise
    # Side effeccts:
    # This function doesn't print anything or have any other side-effects
    return special_string in text
