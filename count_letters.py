# count_letters.py

def count_letters(text):
    """
    This function takes a string and counts how many times each letter appears.
     It count letters (A–Z and a–z). Lowercase and uppercase
     count as the same letter. All the keys in the dictionary will be Uppercase letters. If the string
     is empty or has no letters, return an empty dictionary.
    """

    # This list will store our results.
    letter_counts = {}

    # Go through each character in the string one by one
    for i in text:

        # Check if the character is a lowercase letter (a-z)
        if 'a' <= i <= 'z':
            # Convert lowercase to uppercase so everything is counted the same way
            upper_i = chr(ord(i) - 32)

        # Check if the character is an uppercase letter (A-Z)
        elif 'A' <= i <= 'Z':
            upper_i = i

        else:
            # If it's not a letter (ex: number, space, punctuation), skip it
            continue

        # Update the list
        # If we've never seen this letter before, start its count at 1
        if upper_i not in letter_counts:
            letter_counts[upper_i] = 1
        else:
            # If we HAVE seen it, just add 1 to the current count
            letter_counts[upper_i] += 1

    # After checking every character, return the final counts
    return letter_counts

#print(count_letters("12345!!!"))