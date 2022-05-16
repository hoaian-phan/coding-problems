""" Given a string s, find the length of the longest substring without repeating characters."""


def length_of_longest_substring(s):
    """ Return the length of the longest substring without repeating characters
    
    >>> length_of_longest_substring("")
    0
    >>> length_of_longest_substring("a")
    1
    >>> length_of_longest_substring("bbbbb")
    1
    >>> length_of_longest_substring("abcabcbb")
    3
    >>> length_of_longest_substring("pwwkew")
    3
    """

    # Edge cases: If the input string is empty or has only one character, its length is also
    # the length of the longest substring without repeating characters
    if len(s) <= 1:
        return len(s)

    # Otherwise, create a variable longest to store the length of the longest substring without
    # repeating characters called longest. 
    longest = 0
    
    # Create a set to store all seen characters in the string
    seen_set = set()

    # Use 2 pointers to keep track of the positions of the characters
    # i is the pointer to the position of the character at current iteration of the input string
    # j is the pointer to the position of the character of the substring
    i = 0
    j = 0

    # Run the while loops until the end of the input string, check if the character is already seen
    # if the character is not already seen -> add it to the seen set, and update the longest variable 
    # by finding the max of current longest versus the length of the seen set, 
    # and increment i to move to the next character
    while i < len(s):
        if s[i] not in seen_set:
            seen_set.add(s[i])
            longest = max(longest, len(seen_set))
            i += 1
        # otherwise, if the character is seen, remove the character at the position j of the substring,
        # and increment j to move to the next character
        else:
            seen_set.remove(s[j])
            j += 1
        
    # When the while loop exits, return the longest variable
    return longest


# Runtime: O(n)
# Spacetime: O(n)

# Running doctest
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)