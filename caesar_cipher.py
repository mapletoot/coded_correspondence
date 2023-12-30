'''
Pseudo code:
# Create a list called alphabet storing the alphabet.
# This list will be used as a reference for the characters in the messages that we want to encode/decode.
# Write a function that encodes a message.
# The function will iterate through characters in a message to encode,
# it will find the index of each character in the message from the alphabet string,
# move the index by however many places the caesar shift requires,
# and then append the letter at the new index to a new decoded message string.
# The decode function will work in the same way, but use the encode shift * -1 as the decode shift
'''

alphabet = "abcdefghijklmnopqrstuvwxyz"

# asking for inputs and converting string to lower case as the alphabet is in lower case
encode_or_decode = input("Are you encoding a message? Type y/n: ").lower()
while encode_or_decode != "y" and encode_or_decode != "n":
    encode_or_decode = input(
        "Please enter 'y' if you are encoding a message and 'n' if you are decoding a message: ").lower()

if encode_or_decode == "y":
    message = input("What message do you want to encode? ").lower()
    offset_value = int(input('''What caesar shift value would you like to use to encode your message? \n If you want A to become B please enter 1 or -25. \nIf you want B to become A please enter -1 or 25. \netc.
    '''))
else:
    message = input("What message are you decoding? ").lower()
    offset_value = -1 * int(input('''What caesar shift value was used to encode the message?
    If A became B please enter 1 or -25.
    If B became A please enter -1 or 25.
    etc.
    '''))


def caesar_shift(message_function, offset_value_function):
    ''' This function takes a message and shift value as an input and returns
    the decoded message
    '''
    shifted_message = ""
    for letter in message_function:
        # This part changes all the letters in the string by the shift amount and adds to encoded message string
        if letter in alphabet:
            position = alphabet.find(letter)
            new_character = alphabet[(position + offset_value_function) % 26]
            shifted_message += new_character

        # This part leaves the spaces and other characters alone and adds them to encoded message string
        else:
            new_character = letter
            shifted_message += new_character
    print(f"Your old message was {message_function}")
    print(f"Your new message is {shifted_message}")
    return shifted_message
