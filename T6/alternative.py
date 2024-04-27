def alternate_uppercase(word_string):
    result = ""
    for index, char in enumerate(word_string):
        # Check if the index is odd (since indexing starts from 0)
        if index % 2 == 1:
            # Convert the character to uppercase and append to the result
            result += char.upper()
        else:
            # Append the character as it is
            result += char
    return result

# Example usage:
word_string = input("Enter a string: ")
converted_string = alternate_uppercase(word_string)
print("Converted string:", converted_string)

def alternate_word_uppercase(word_string):
    result = ""
    words = word_string.split()  # Split the input string into words
    for index, word in enumerate(words):
        # Check if the index is odd
        if index % 2 == 1:
            # Convert the word to uppercase and append to the result
            result += word.upper()
        else:
            # Append the word as it is
            result += word
        # Add a space after each word, except for the last one
        if index != len(words) - 1:
            result += " "
    return result

# Example usage:
word_string = input("Enter a string: ")
converted_string = alternate_word_uppercase(word_string)
print("Converted string:", converted_string)