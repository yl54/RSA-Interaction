"""
This module provides helper functions for RSA message transferring.

"""

import Algorithms

# Function to start an interaction session.
def interact(p, q, N, phi, e, d):
    encrypted_messages = []
    ref_ch_to_int, ref_int_to_ch = assignChCodesOrig()
    while True:
        choice = raw_input("Type 'message' to add a message, \n  'decrypt' to decrypt the next message,\n  or 'exit' to stop interacting: ")  
        if choice == "message" :
            m_encrypts = handleMessage(N, e, ref_ch_to_int)
            encrypted_messages.append(m_encrypts)
        elif choice == "decrypt":
            if len(encrypted_messages) == 0:
                print "Message queue is empty."
            else:
                m_encrypts = encrypted_messages.pop(0)
                m_decrypt = handleDecrypt(N, d, ref_int_to_ch, m_encrypts)
        elif choice == "exit":
            print "Requested exit."
            break;
        else:
            print "Please type one of the specified options."

# Function to handle message choice.
def handleMessage(N, e, ref_ch_to_int):
    m = raw_input("Enter a message (a-z characters): ")
    m_encrypts = encryptMessage(m, N, e, ref_ch_to_int)
    print "Raw message: " + m
    print "Encrypted message: " + str(m_encrypts)
    return m_encrypts

# Function to handle decrypt choice.
def handleDecrypt(N, d, ref_int_to_ch, m_encrypts):
    words = []
    m_decrypt = decryptMessage(m_encrypts, N, d, ref_int_to_ch)
    words.append(m_decrypt)
    print "Encrypted message: " + m_encrypt
    print "Decrypted message: " + m_decrypt
    end_val = " ".join(words)
    return end_val

# Function to encrypt message.
def encryptMessage(m, N, e, ref_ch_to_int):
    conversion = convertMessageToInt(m, ref_ch_to_int)
    # Compute m_encrypt = conversion^e mod n.
    m_encrypts = []
    for i in xrange(0, len(conversion), 1):
        m_encrypt = Algorithms.calcLargeMod(conversion[i], e, N)
        m_encrypts.append(m_encrypt)
        # print "m: " + m
        # print "conversion: " + str(conversion)
        # print "m_encrypt: " + str(m_encrypt)
    return m_encrypts

# Function to decrypt message.
def decryptMessage(m_encrypts, N, d, ref_int_to_ch):
    # Compute m_decrypt = m_encrypt^d mod n
    conversions = []
    for i in xrange(0, len(m_encrypts), 1):
        m_encrypt = m_encrypts[i]
        m_decrypt = Algorithms.calcLargeMod(m_encrypt, d, N)
        # print "m_encrypt: " + str(m_encrypt)
        # print "m_decrypt: " + str(m_decrypt)
        conversion = convertIntToMessage(m_decrypt, ref_int_to_ch)
        conversions.append(conversion)
        # print "conversion: " + conversion
    return " ".join(conversions)

# Function to decrypt message with signature.
def decryptMessageSig(m_encrypts, N, d, ref_int_to_ch, sig, e):
    # Compute m_decrypt = m_encrypt^d mod n
    conversions = []
    for i in xrange(0, len(m_encrypts), 1):
        m_encrypt = m_encrypts[i]
        m_decrypt = Algorithms.calcLargeMod(m_encrypt, d, N)
        conversion = convertIntToMessage(m_decrypt, ref_int_to_ch)
        conversions.append(conversion)
        # print "m_encrypt: " + str(m_encrypt)
        # print "m_decrypt: " + str(m_decrypt)
        # print "conversion: " + conversion
    # This part will calculate the original signature to see 
    #   if it came from the correct sender.
    m_orig_hash = Algorithms.calcLargeMod(sig, e, N)
    # print "m_orig_hash: " + str(m_orig_hash)
    # print "-----------------------"
    return " ".join(conversions)

# Function to convert a string into an integer.
def convertMessageToInt(val, ref_ch_to_int):
    if val is None:
        return None
    pieces = []
    words = []
    t = 0
    for i in xrange(0, len(val), 1):
        if val[i] == ' ' or t >=3:
            pieces.append(words)
            words = []
            t = 0
            if val[i] != ' ':
                words.append(ref_ch_to_int[val[i]])
        else:
            words.append(ref_ch_to_int[val[i]])
        t += 1
    pieces.append(words)
    full_val = []
    for i in xrange(0, len(pieces), 1):
        p = pieces[i]
        s_val = "".join(p)
        if s_val == '':
            continue
        i_val = int(s_val)
        full_val.append(i_val)
        # print "int pieces: " + ", ".join(p)
    return full_val

# Function to convert an integer into an string.
def convertIntToMessage(val, ref_int_to_ch):
    if val is None:
        return None
    str_val = str(val)
    pieces = []
    beg = 0
    if len(str_val) % 2 == 1:
        beg = 1
        pieces.append(ref_int_to_ch["0" + str_val[0]])
    for i in xrange(beg, len(str_val) - 1, 2):
        pieces.append(ref_int_to_ch[str_val[i:i+2]])
    full_val = "".join(pieces)
    # print "str_val: " + str_val
    # print "string pieces: " + ", ".join(pieces)
    # print "full_val: " + full_val
    return full_val

# Function to assign codes to each character.
def assignChCodesOrig():
    ref_ch_to_int = {}
    ref_int_to_ch = {}

    # 0 - 26 representation
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

# Function to assign codes to each character.
#   This is the ascii representation.
def assignChCodesOAscii():
    ref_ch_to_int = {}
    ref_int_to_ch = {}
    
    ref_ch_to_int['a'] = '65'
    ref_ch_to_int['b'] = '66'
    ref_ch_to_int['c'] = '67'
    ref_ch_to_int['d'] = '68'
    ref_ch_to_int['e'] = '69'
    ref_ch_to_int['f'] = '70'
    ref_ch_to_int['g'] = '71'
    ref_ch_to_int['h'] = '72'
    ref_ch_to_int['i'] = '73'
    ref_ch_to_int['j'] = '74'
    ref_ch_to_int['k'] = '75'
    ref_ch_to_int['l'] = '76'
    ref_ch_to_int['m'] = '77'
    ref_ch_to_int['n'] = '78'
    ref_ch_to_int['o'] = '79'
    ref_ch_to_int['p'] = '80'
    ref_ch_to_int['q'] = '81'
    ref_ch_to_int['r'] = '82'
    ref_ch_to_int['s'] = '83'
    ref_ch_to_int['t'] = '84'
    ref_ch_to_int['u'] = '85'
    ref_ch_to_int['v'] = '86'
    ref_ch_to_int['w'] = '87'
    ref_ch_to_int['x'] = '88'
    ref_ch_to_int['y'] = '89'
    ref_ch_to_int['z'] = '90'
    
    ref_int_to_ch['65'] = 'a'
    ref_int_to_ch['66'] = 'b'
    ref_int_to_ch['67'] = 'c'
    ref_int_to_ch['68'] = 'd'
    ref_int_to_ch['69'] = 'e'
    ref_int_to_ch['70'] = 'f'
    ref_int_to_ch['71'] = 'g'
    ref_int_to_ch['72'] = 'h'
    ref_int_to_ch['73'] = 'i'
    ref_int_to_ch['74'] = 'j'
    ref_int_to_ch['75'] = 'k'
    ref_int_to_ch['76'] = 'l'
    ref_int_to_ch['77'] = 'm'
    ref_int_to_ch['78'] = 'n'
    ref_int_to_ch['79'] = 'o'
    ref_int_to_ch['80'] = 'p'
    ref_int_to_ch['81'] = 'q'
    ref_int_to_ch['82'] = 'r'
    ref_int_to_ch['83'] = 's'
    ref_int_to_ch['84'] = 't'
    ref_int_to_ch['85'] = 'u'
    ref_int_to_ch['86'] = 'v'
    ref_int_to_ch['87'] = 'w'
    ref_int_to_ch['88'] = 'x'
    ref_int_to_ch['89'] = 'y'
    ref_int_to_ch['90'] = 'z'
    
    return ref_ch_to_int, ref_int_to_ch

