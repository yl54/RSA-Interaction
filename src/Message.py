import Algorithms

"""
This module provides helper functions for RSA message transferring.

"""

# Function to start an interaction session.
def interact(p, q, N, phi, e, d):
    encrypted_messages = []
    ref_ch_to_int, ref_int_to_ch = assignChCodes()
    while True:
        choice = raw_input("Type 'message' to add a message, \
                                 'decrypt' to decrypt the next message, or \
                                 'exit' to stop interacting.")  
        if(choice == "message"):
            m_encrypt = handleMessage(N, e, ref_ch_to_int)
            encrypted_messages.append(m_encrypt)
        else if(choice == "decrypt"):
            if(len(encrypted_messages) == 0):
                print "Message queue is empty."
            else:
                m_encrypt = encrypted_messages.pop(0)
                m_decrypt = handleDecrypt(m_encrypt, N, d, ref_int_to_ch)
        else if(choice == "exit"):
            print "Requested exit."
            break;
        else:
            print "Please type one of the specified options."

# Function to handle message choice.
def handleMessage(N, e, ref_ch_to_int):
    m = raw_input("Enter a message (a-z characters): ")
    m_encrypt = Message.encryptMessage(m, N, e, ref_ch_to_int)
    print "Raw message: " + m
    print "Encrypted message: " + m_encrypt
    return m_encrypt

# Function to handle decrypt choice.
def handleDecrypt(m_encrypt, N, d, ref_int_to_ch):
    m_decrypt = Message.decryptMessage(m_encrypt, N, d, ref_int_to_ch)
    print "Encrypted message: " + m_encrypt
    print "Decrypted message: " + m_decrypt
    return m_decrypt

# Function to encrypt message.
# Q: How to break up a big message into multiple messages?
def encryptMessage(m, N, e, ref_ch_to_int):
    # Convert raw message into an integer.
    
    # Compute m_encrypt = m^e mod n.
    
    # Return m_encrypt.

# Function to decrypt message.
def decryptMessage(m_encrypt, N, d, ref_int_to_ch):
    # Compute m_decrypt = m_encrypt^d mod n
    
    # Convert m_decrypt to plain text.

# Function to convert a string into an integer.
def convertMessageToInt(input):
    # Check if input is valid.

    # Concactenate a string that is the integer representation of input.

    # Use a python lib to convert string to int.

# Function to convert an integer into an string.
def convertIntToMessage(input):
    # Check if input is valid.

    # Concactenate a string that takes each 2 digit combination.

    # Return message.

# Function to assign codes to each character.
def assignChCodes():
    ref_ch_to_int = {}
    
    ref_ch_to_int['a'] = '01'
    ref_ch_to_int['b'] = '02'
    ref_ch_to_int['c'] = '03'
    ref_ch_to_int['d'] = '04'
    ref_ch_to_int['e'] = '05'
    ref_ch_to_int['f'] = '06'
    ref_ch_to_int['g'] = '07'
    ref_ch_to_int['h'] = '08'
    ref_ch_to_int['i'] = '09'
    ref_ch_to_int['j'] = '10'
    ref_ch_to_int['k'] = '11'
    ref_ch_to_int['l'] = '12'
    ref_ch_to_int['m'] = '13'
    ref_ch_to_int['n'] = '14'
    ref_ch_to_int['o'] = '15'
    ref_ch_to_int['p'] = '16'
    ref_ch_to_int['q'] = '17'
    ref_ch_to_int['r'] = '18'
    ref_ch_to_int['s'] = '19'
    ref_ch_to_int['t'] = '20'
    ref_ch_to_int['u'] = '21'
    ref_ch_to_int['v'] = '22'
    ref_ch_to_int['w'] = '23'
    ref_ch_to_int['x'] = '24'
    ref_ch_to_int['y'] = '25'
    ref_ch_to_int['z'] = '26'
    
    ref_int_to_ch = {}
    ref_int_to_ch['01'] = 'a'
    ref_int_to_ch['02'] = 'b'
    ref_int_to_ch['03'] = 'c'
    ref_int_to_ch['04'] = 'd'
    ref_int_to_ch['05'] = 'e'
    ref_int_to_ch['06'] = 'f'
    ref_int_to_ch['07'] = 'g'
    ref_int_to_ch['08'] = 'h'
    ref_int_to_ch['09'] = 'i'
    ref_int_to_ch['10'] = 'j'
    ref_int_to_ch['11'] = 'k'
    ref_int_to_ch['12'] = 'l'
    ref_int_to_ch['13'] = 'm'
    ref_int_to_ch['14'] = 'n'
    ref_int_to_ch['15'] = 'o'
    ref_int_to_ch['16'] = 'p'
    ref_int_to_ch['17'] = 'q'
    ref_int_to_ch['18'] = 'r'
    ref_int_to_ch['19'] = 's'
    ref_int_to_ch['20'] = 't'
    ref_int_to_ch['21'] = 'u'
    ref_int_to_ch['22'] = 'v'
    ref_int_to_ch['23'] = 'w'
    ref_int_to_ch['24'] = 'x'
    ref_int_to_ch['25'] = 'y'
    ref_int_to_ch['26'] = 'z'
    
    return ref_ch_to_int, ref_int_to_ch


    


