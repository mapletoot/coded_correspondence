'''
Pseudo code:
# Create a list called alphabet storing the alphabet.
# This list will be used as a reference for the characters in the messages that we want to encode/decode.
# Write a function that decodes a message.
# The function will iterate through characters in a message to decode,
# it will find the index of each character in the message from the alphabet string,
# move the index by however many places the caesar shift requires,
# and then append the letter at the new index to a new decoded message string.
'''

alphabet = "abcdefghijklmnopqrstuvwxyz"

# asking for inputs and converting string to lower case as the alphabet is in lower case
message = input("What message would you like to encode? ").lower()
caesar_shift = int(input("What caesar shift value would you like to use? "))


def decode_caesar(coded_message, decode_shift):
    ''' This function takes a message and shift value as an input and returns
    the decoded message
    '''
    decoded_message = ""
    for letter in coded_message:
        if letter in alphabet:
            position = alphabet.find(letter)
            new_character = alphabet[(position + decode_shift) % 26]
            decoded_message += new_character
        else:
            new_character = letter
            decoded_message += new_character
    return decoded_message


print(decode_caesar(message, caesar_shift))
