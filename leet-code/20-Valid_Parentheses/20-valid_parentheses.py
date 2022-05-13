""" Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

# My Solution
def is_valid(s):
    """ Return True if the input string is valid 
    >>> is_valid("")
    True
    >>> is_valid("(")
    False
    >>> is_valid("]")
    False
    >>> is_valid("()[]{}")
    True
    >>> is_valid("(]")
    False
    """
    # create a dictionary with keys being the closing marks and values being the opening marks
    marks = {")": "(", "}": "{", "]": "["}
    # create a list to keep track of opening marks seen (this list is an implementation of a stack)
    seen = []
    # iterate through the input string, if seeing an opening mark -> add it to the seen list
    # otherwise (means seeing the closing mark), if there is nothing in the seen list -> return False
    # or if the last element in the seen list is the corresponding mark -> pop it out of the seen list
    # otherwise (means the last element is not the correct opening mark) -> return False
    for item in s:
        if item in marks.values():
            seen.append(item)
        else:
            if not seen:
                return False
            if seen[-1] == marks[item]:
                seen.pop()
            else:
                return False

    # After going through the whole string, if the seen list still has opening marks left -> 
    # return False
    return not seen

# Runtime: O(n)
# Spacetime: O(n)

# Running doctest
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)
        