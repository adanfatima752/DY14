import re

def matches_pattern(string, pattern):
    """
    Checks if the given string matches the pattern where:
    - Letters in the pattern correspond to any alphabetical character.
    - Numbers in the pattern correspond to any digit.
    
    Args:
    - string: The string to check.
    - pattern: The pattern to match against. Letters correspond to alphabetic characters, numbers to digits.
    
    Returns:
    - True if the string matches the pattern, otherwise False.
    """
    # Convert the pattern to a regular expression
    regex_pattern = ''.join(
        '[a-zA-Z]' if char.isalpha() else
        '\d' if char.isdigit() else
        re.escape(char)  # Escape any other characters
        for char in pattern
    )
    
    # Compile the regular expression
    regex = re.compile(f'^{regex_pattern}$')
    
    # Match the string against the pattern
    return bool(regex.match(string))

# Example usage:
string = "a1b2"
pattern = "a1b2"
print(matches_pattern(string, pattern))  # Output: True

string = "a1b23"
pattern = "a1b2"
print(matches_pattern(string, pattern))  # Output: False
