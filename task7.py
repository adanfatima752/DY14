import re
from collections import Counter

def clean_string(s):
    # Remove non-alphanumeric characters and convert to lowercase
    return re.sub(r'[^a-zA-Z0-9]', '', s).lower()

def are_anagrams(str1, str2):
    # Clean the strings
    cleaned_str1 = clean_string(str1)
    cleaned_str2 = clean_string(str2)
    
    # Create frequency dictionaries for both cleaned strings
    freq1 = Counter(cleaned_str1)
    freq2 = Counter(cleaned_str2)
    
    # Check if they are anagrams
    are_anagrams = freq1 == freq2
    
    # Prepare result dictionary
    result = {
        'are_anagrams': are_anagrams,
        'frequencies_str1': freq1,
        'frequencies_str2': freq2
    }
    
    return result

# Example usage:
string1 = "Listen, 123!"
string2 = "Silent 321."

result = are_anagrams(string1, string2)
print(result)
