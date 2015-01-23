# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:


#Removes anything that is not string and uppercases it
def clean_message(input_message):
    '''
    (str) -> str
    
    >>> clean_message('utr45,;kgj')
    'UTRKGJ'
    >>> clean_message('ioehioh758gh565;.g')
    'IOEHIOHGHG'
    
    Returns only the string values, uppercased, in the given parameter
    '''
    cleaned_message = ''
    
    #checks each character if its string
    for char in input_message:
        if char.isalpha():
            cleaned_message += char
    #uppercase the message
    cleaned_message = cleaned_message.upper()
    return cleaned_message


#Encrypts the letter by adding keysteam to letter
def encrypt_letter(upper_letter, keystream):
    '''
    (str, int) -> str
    
    >>> encrypt_letter('L', 12)
    'X'
    >>> encrypt_letter('Y', 14)
    'M'
    >>> encrypt_letter('A', 20)
    'U'
    
    Returns the encrpyed letter by adding the value of char to the keystream
    and finding what letter holds that value
    '''
    #convert the given letter to actual value of letter
    upper_letter_value = ord(upper_letter) - 65
    encrypted_letter_value = upper_letter_value + keystream
    if encrypted_letter_value >= 26:
        encrypted_letter_value = encrypted_letter_value - 26
    #encrypts the letter by turning it to ascii
    encrypted_upper_letter = chr(65 + encrypted_letter_value)
    return encrypted_upper_letter


#Decrypts the letter by applying keystream to letter
def decrypt_letter(upper_letter, keystream):
    '''
    (str, int) -> str
    
    >>> decrypt_letter('X', 12)
    'L'
    >>> decrypt_letter('D', 25)
    'E'
    
    Returns the decrypt letter by converting upper_letter to actual value, then
    subtracts the result by keystream, then converts it back to ascii
    '''
    #converts letter to the actual letter value
    upper_letter_value = ord(upper_letter) - 65
    decrypt_letter_value = upper_letter_value - keystream
    if decrypt_letter_value < 0:
        decrypt_letter_value = decrypt_letter_value + 26
    #decrypts the letter by turning it to ascii
    decrypted_upper_letter = chr(65 + decrypt_letter_value)
    return decrypted_upper_letter


#swaps the card at given index with next card
def swap_cards(card_list, index):
    '''
    (list of int, int) -> NoneType
    
    >>> temp_list = [1, 2 ,3 ,4, 5]
    >>> swap_cards(temp_list, 2)
    >>> temp_list
    [1, 2, 4, 3, 5]
    
    >>> temp_list = [1, 2, 3, 4, 5]
    >>> swap_cards(temp_list, 4)
    >>> temp_list
    [5, 2, 3, 4, 1]
    
    Mutates the list by swaping the index of the list by the next index
    '''
    #Case 1: if the index is last, then swap it with the first card
    if index == len(card_list)-1:
        temp = card_list[index]
        card_list[index] = card_list[0]
        card_list[0] = temp
    #Case 2: swap with the next card
    else:
        temp = card_list[index]
        card_list[index] = card_list[index+1]
        card_list[index+1] = temp


#Step 1: move JOKER1 with next card
def move_joker_1(card_list):
    '''
    (list of int) -> NoneType
    
    >>> temp_list = [1,2,3,27]
    >>> move_joker_1(temp_list)
    >>> temp_list
    [27, 2, 3, 1]
    
    >>> temp_list = [1, 2, 27, 5, 6]
    >>> move_joker_1(temp_list)
    >>> temp_list
    [1, 2, 5, 27, 6]
    
    Mutates the list by swaping JOKER1 with next card
    '''
    index = card_list.index(JOKER1)
    swap_cards(card_list, index)


#Step 2: swap JOKER2 with the next 2 cards
def move_joker_2(card_list):
    '''
    (list of int) -> NoneType
    
    >>> temp_list = [1, 2, 3, 28]
    >>> move_joker_2(temp_list)
    >>> temp_list
    [2, 28, 3, 1]
    >>> temp_list = [1, 2, 28, 3, 5]
    >>> move_joker_2(temp_list)
    >>> temp_list
    [1, 2, 3, 5, 28]
    
    Mutates the list by swapping JOKER2 with next 2 cards
    '''
    #Move joker 2 once
    index = card_list.index(JOKER2)
    swap_cards(card_list, index)
    #Move joker 2 again, this will move joekr 2 with next 2 cards
    index = card_list.index(JOKER2)
    swap_cards(card_list, index)


#Step 3: performing a triple cut to the card list
def triple_cut(card_list):
    '''
    (list of int) -> NoneType
    
    >>> temp_list = [1, 2, 4, 27, 3, 12, 28, 9, 5, 7]
    >>> triple_cut(temp_list)
    >>> temp_list
    [9, 5, 7, 27, 3, 12, 28, 1, 2, 4]
    
    >>> temp_list = [1, 2, 4, 28, 3, 12, 27, 9, 5, 7]
    >>> triple_cut(temp_list)
    >>> temp_list
    [9, 5, 7, 28, 3, 12, 27, 1, 2, 4]
    
    >>> temp_list = [27, 1, 4, 28, 2, 5]
    >>> triple_cut(temp_list)
    >>> temp_list
    [2, 5, 27, 1, 4, 28]
    
    >>> temp_list = [28, 1, 4, 27]
    >>> triple_cut(temp_list)
    >>> temp_list
    [28, 1, 4, 27]
    
    REQ: JOKER1 and JOKER2 present in list of int
    
    Mutates list by moving everything above the first joker to the bottom of
    the deck and moving everything below the second joker to the top of the
    deck
    '''
    index_joker_1 = card_list.index(JOKER1)
    index_joker_2 = card_list.index(JOKER2)
    
    #Case 1: joker 1 index is less than joker 2
    if index_joker_1 < index_joker_2:
        #splits the list into 3 parts, from beginning to joker 1, joker 1 to
        #joker 2 then joker 2 to end
        first_half = card_list[:index_joker_1]
        second_half = card_list[index_joker_1:index_joker_2+1]
        third_half = card_list[index_joker_2+1:]
        
        #stores the list by adding previous lists in reverse order
        card_list[:index_joker_1] = third_half
        
        index_joker_1 = card_list.index(JOKER1)
        index_joker_2 = card_list.index(JOKER2)
        
        card_list[index_joker_1:index_joker_2+1] = second_half
        
        index_joker_1 = card_list.index(JOKER1)
        index_joker_2 = card_list.index(JOKER2)
        
        card_list[index_joker_2+1:] = first_half
    #Case 2: joker 1 index is greater than joker 2
    else:
        #splits the list into 3 parts, from beginning to joker 2, joker 2 to
        #joker 1 then joker 1 to end
        first_half = card_list[:index_joker_2]
        second_half = card_list[index_joker_2:index_joker_1+1]
        third_half = card_list[index_joker_1+1:]
        
        #stores the list by adding previous lists in reverse order
        card_list[:index_joker_2] = third_half
        
        index_joker_1 = card_list.index(JOKER1)
        index_joker_2 = card_list.index(JOKER2)
        
        card_list[index_joker_2:index_joker_1+1] = second_half
        
        index_joker_1 = card_list.index(JOKER1)
        index_joker_2 = card_list.index(JOKER2)
        
        card_list[index_joker_1+1:] = first_half


#Step 4: Looks at the last card and moves that many cards from the top to
#the bottom but before the last card
def insert_top_to_bottom(card_list):
    '''
    (list of int) -> NoneType
    
    >>> temp_list = [5, 6, 2, 27, 8, 28, 3, 1]
    >>> insert_top_to_bottom(temp_list)
    >>> temp_list
    [6, 2, 27, 8, 28, 3, 5, 1]
    
    Mutates the list by looking at the last int of card_list, removing that
    many numbers from the top list and adding them just before the last card
    '''
    #get last card number
    last_card = card_list[-1]
    #special case: if bottom card is JOKER2, then use JOKER1 as number of cards
    if last_card == JOKER2:
        last_card = JOKER1
    #get the cards from top to the last card number in a list
    to_bottom = card_list[:last_card]
    #deletes the all the cards from top to the last card
    del card_list[:last_card]
    #adds the cards from top to last card to the card_list but before last card
    card_list[-1:0] = to_bottom


#Step 5: considers the top card as an index, then finds the card at that index
def get_card_at_top_index(card_list):
    '''
    (list of int) -> int
    
    >>> get_card_at_top_index([3, 25, 4, 6, 27, 8, 28])
    6
    >>> get_card_at_top_index([5, 20, 17, 7, 19, 28, 9, 17, 10]) 
    28
    
    Returns the value of the card at which the top card is considered as an
    index, and looks at that index in card_list
    '''
    #get top cards value as an index
    top_index = card_list[0]
    #special case: if top card is JOKER2, use JOKER1 as index
    if top_index == JOKER2:
        top_index = JOKER1
    #find the card at that top cards value
    found_card = card_list[top_index]
    
    return found_card


#does all the steps from 1-5
def get_next_value(card_list):
    '''
    (list of int) -> int
    
    >>> get_next_value([1, 2, 3, 4, 28, 5, 6, 7, 27, 8, 9])
    4
    >>> get_next_value([4, 5, 3, 2, 7, 10, 27, 28, 6, 9])
    10
    
    Returns the next potenial keystream value by going through Steps 1-5
    '''
    #step 1 of algorithm
    move_joker_1(card_list)
    #step 2 of algorithm
    move_joker_2(card_list)
    #step 3 of algorithm
    triple_cut(card_list)
    #step 4 of algorithm
    insert_top_to_bottom(card_list)
    #step 5 of algorithm and returns the result
    return get_card_at_top_index(card_list)


#runs until potential keystream value is a keystream value
def get_next_keystream_value(card_list):
    '''
    (list of int) -> int
    
    >>> get_next_keystream_value([1, 2, 3, 4, 28, 5, 6, 7, 27, 8, 9])
    4
    >>> get_next_keystream_value([4, 5, 3, 2, 7, 10, 27, 28, 6, 9])
    10
    
    Returns the next keystream value (1-26) by running until it does so
    '''
    #runs until a real keystream is found
    value = get_next_value(card_list)
    while value == JOKER1 or value == JOKER2:
        value = get_next_value(card_list)
    return value


#encrypts or decrypts a message
def process_message(card_list, message, mode):
    '''
    (list of int, str, str) -> str
    
    >>> deck = read_deck(open('deck1.txt'))
    >>> process_message(deck, 'hello!', 'e')
    'SNISY'
    >>> deck = read_deck(open('deck1.txt'))
    >>> process_message(deck, 'SNISY', 'd')
    'HELLO'
    
    REQ: card_list to be length of 28
    
    Returns the encrypted or decrypted by using card_list to get keystream
    value and applying it to message. 'e' for encrypt and 'd' for decrypt
    '''
    #cleans the message
    message = clean_message(message)
    result = ''
    #encrypt the message by getting keystream value and using it
    #to encrypt letter using encrypt_letter
    if mode == 'e':
        for char in message:
            keystream_value = get_next_keystream_value(card_list)
            result += encrypt_letter(char, keystream_value)
    #decrypt the message by getting keystream value and using it
    #to decrypt letter using decrypt_letter
    else:
        for char in message:
            keystream_value = get_next_keystream_value(card_list)
            result += decrypt_letter(char, keystream_value)
    return result


#encrypts or decrypts a list of messages
def process_messages(card_list, message_list, mode):
    '''
    (list of int, list of str, str) -> list of str
    
    >>> deck = read_deck(open('deck1.txt'))
    >>> process_messages(deck, ['hello', 'bye'], 'e')
    ['SNISY', 'AJP']
    >>> deck = read_deck(open('deck1.txt'))
    >>> process_messages(deck, ['SNISY', 'AJP'], 'd')
    ['HELLO', 'BYE']
    
    REQ: card_list to be length of 28
    
    Returns a list of encrypted or decrypted messages by calling
    process_message(card_list, message, mode) for each message
    '''
    result = []
    #calls process_message for each message and appends it to a list
    for char in message_list:
        result_message = process_message(card_list, char, mode)
        result.append(result_message)
    return result


#reads messages from a txt file
def read_messages(opened_file):
    '''
    (IO.TextIOWrapper) -> list of str
    
    Returns the messages in opened_file for each line as a message
    '''
    messages = []
    
    #reads each line and checks if its a valid line. if yes, strips 'new line'
    for line in opened_file:
        if line != '':
            line = line.strip('\n')
            messages.append(line)
    return messages


#reads a deck of cards from a txt file
def read_deck(opened_file):
    '''
    (IO.TextIOWrapper) -> list of int
    
    Returns a list of numbers from 1-28 by reading opened_file
    '''
    
    deck = []
    temp = ''
    #reads every line and stores it in a variable to edit with
    for line in opened_file:
        if line != '':
            line = line.strip()
            temp += line
            temp += ' '  #adds new blank space to seperate the next number
    deck = temp.split()
    #converts all str to ints
    for i in range(0, len(deck)):
        deck[i] = int(deck[i])
                    
    return deck