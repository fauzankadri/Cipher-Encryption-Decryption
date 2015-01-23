"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message1.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    #reads the deck using cipher_functions.read_deck by opening the txt file
    opened_deck_file = open(DECK_FILENAME, 'r')
    deck = cipher_functions.read_deck(opened_deck_file)
    opened_deck_file.close
    
    #reads the message using cipher_functions.read_message by opening the txt
    #file
    opened_message_file = open(MSG_FILENAME, 'r')
    message = cipher_functions.read_messages(opened_message_file)
    opened_message_file.close

    #uses cipher_function.process_messages to return the encrypt/decrypt
    #result and stores it
    result = cipher_functions.process_messages(deck, message, MODE)
    #prints every message in new line
    for i in range(0, len(result)):
        print(result[i])

main()