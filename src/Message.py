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
        if choice == "message" :
            # Need to handle split up messages.
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
    m_encrypts = Message.encryptMessage(m, N, e, ref_ch_to_int)
    # print "Raw message: " + m
    # print "Encrypted message: " + str(m_encrypts)
    return m_encrypts

# Function to handle decrypt choice.
def handleDecrypt(N, d, ref_int_to_ch, m_encrypts):
    words = []
    for i in xrange(0, len(m_encrypts), 1):
        m_decrypt = Message.decryptMessage(m_encrypt, N, d, ref_int_to_ch)
        words.append(m_decrypt)
        print "Encrypted message: " + m_encrypt
        print "Decrypted message: " + m_decrypt
    end_val = " ".join(words)
    return end_val

# Function to encrypt message.
# Q: How to break up a big message into multiple messages?
def encryptMessage(m, N, e, ref_ch_to_int):
    conversion = convertMessageToInt(m, ref_ch_to_int)
    # Compute m_encrypt = conversion^e mod n.
    m_encrypts = []
    for i in xrange(0, len(conversion), 1):
        m_encrypt = Algorithms.calcLargeMod(conversion[i], e, N)
        m_encrypts.append(m_encrypt)
        #print "m: " + m
        #print "conversion: " + str(conversion)
        print "m_encrypt: " + str(m_encrypt)
        # do the signing part here.
    return m_encrypts

# Function to decrypt message.
def decryptMessage(m_encrypts, N, d, ref_int_to_ch):
    # Compute m_decrypt = m_encrypt^d mod n
    conversions = []
    for i in xrange(0, len(m_encrypts), 1):
        m_encrypt = m_encrypts[i]
        m_decrypt = Algorithms.calcLargeMod(m_encrypt, d, N)
        conversion = convertIntToMessage(m_decrypt, ref_int_to_ch)
        conversions.append(conversion)
        print "m_encrypt: " + str(m_encrypt)
        print "m_decrypt: " + str(m_decrypt)
        print "conversion: " + conversion
    return " ".join(conversions)

# Function to decrypt message with signature.
def decryptMessageSig(m_encrypts, N, d, ref_int_to_ch, sig, e):
    # Compute m_decrypt = m_encrypt^d mod n
    conversions = []
    for i in xrange(0, len(m_encrypts), 1):
        m_encrypt = m_encrypts[i]
        m_decrypt = Algorithms.calcLargeMod(m_encrypt, d, N)
        print "m_encrypt: " + str(m_encrypt)
        print "m_decrypt: " + str(m_decrypt)
        
        conversion = convertIntToMessage(m_decrypt, ref_int_to_ch)
        conversions.append(conversion)
        print "conversion: " + conversion

        # do the sign part here.
        m_orig = Algorithms.calcLargeMod(sig, e, N)
        print "m_orig: " + str(m_orig)
        print "-----------------------"
    return " ".join(conversions)

# Function to convert a string into an integer.
def convertMessageToInt(val, ref_ch_to_int):
    if val is None:
        return None
    pieces = []
    words = []
    for i in xrange(0, len(val), 1):
        if val[i] == ' ':
            pieces.append(words)
            words = []
        else:
            words.append(ref_ch_to_int[val[i]])
    pieces.append(words)
    full_val = []
    for i in xrange(0, len(pieces), 1):
        p = pieces[i]
        print "int pieces: " + ", ".join(p)
        s_val = "".join(p)
        i_val = int(s_val)
        full_val.append(i_val)
    return full_val

# Function to convert an integer into an string.
def convertIntToMessage(val, ref_int_to_ch):
    if val is None:
        return None
    str_val = str(val)
    print "str_val: " + str_val
    # Handle case if val is odd number of digits. 
    # Q: Is the single letter case at the beginning or at the end?
    pieces = []
    beg = 0
    if len(str_val) % 2 == 1:
        beg = 1
        pieces.append(ref_int_to_ch["0" + str_val[0]])
    for i in xrange(beg, len(str_val) - 1, 2):
        pieces.append(ref_int_to_ch[str_val[i:i+2]])
    print "string pieces: " + ", ".join(pieces)
    full_val = "".join(pieces)
    print "full_val: " + full_val
    return full_val

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


    


