#ask the user to enter a sentence using the input(0)


str_manip = str(input())

# using the string value, calculate the lenght of str_manip
lenght = len(str_manip)

def replace_last_letter_with_at(str_manip):
    # Split the sentence into words
    words = str_manip.split()

    # Iterate through each word
    for i in range(len(words)):
        # Get the last letter of the word
        last_letter = words[i][-1]

        # Replace the last letter with '@'
        words[i] = words[i][:-1] + '@'

    # Join the modified words back into a sentence
    modified_sentence = ' '.join(words)

    return modified_sentence
