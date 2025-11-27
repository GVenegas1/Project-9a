# count_letters.py

# Project 9a
# Gabriel Venegas
# GitHub username: GVenegas1
# Date: 11/26/2025

def count_letters(text):
    """
    Counts how many times each letter appears in a string.
    """
    letter_counts = {}  # dictionary to store the counts

    # Loop through each character in the text
    for char in text:
        # Convert lowercase to uppercase
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            char = char
        else:
            continue  # skip non-letter characters

        # Count the letter
        if char not in letter_counts:
            letter_counts[char] = 1
        else:
            letter_counts[char] += 1

    return letter_counts


# Testing

if __name__ == "__main__":
    test_string = "Quis custodiet ipsos custodes?"
    print("Testing count_letters() with:", test_string)
    print(count_letters(test_string))
