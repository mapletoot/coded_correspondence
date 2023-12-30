'''psuedo code:
# create an alphabet for reference
# Take a message to encode and a code word as an input. do not allow any characters other than letters and spaces in either input to begin with
# convert all inputs to lower case
# remove space from the code word
'''

# Alphabet for reference
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Messages and code word defined
user_message = "united are boring. Like, really boring"
user_code_word = "goal today now"


def code_word_repeater(message, code_word):
    ''' This function takes the code word and repeats it over and over again
    so that the pattern is the same as the message that needs changing'''

    # remove spaces from the code word
    code_word_no_spaces = code_word.replace(" ", "")

    # Initialise variables to be altered in iteration
    code_word_repeated = ""
    index = 0

    for character in message:
        # If the character is a letter, place the next letter from the code word into the new string
        if character in alphabet:
            code_word_character = index % len(code_word_no_spaces)
            code_word_repeated += code_word_no_spaces[code_word_character]

        # If the character is not a letter, it should mimic the character from the message.
        else:
            code_word_repeated += character
            continue

        # Increase the index before repeating the for loop. This won't be added if the character is not a letter
        index += 1

    print(code_word_repeated)
    return code_word_repeated


code_word_repeater(user_message, user_code_word)
