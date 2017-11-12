import Algorithms
import Message
import Setup

"""
This module implements a complete RSA encryption/decryption 
  interactive session. 

This includes 2 main stages:
- setup
- message transferring.

"""

"""
Reference Guide:
- p, q: user-selected initial primes.
- N: modulus, which is p * q.
- phi: euler's totient for N.
- e: public/encryption exponent.
- d: secret/decryption exponent.
- m_raw: raw message.
- m_encrypt = encrypted message.
- m_decrypt = decrypted message.

"""


"""
Setup: 
- pick two primes p and q.
- calculate phi and n from p and q.
- pick e.
- calculate d from e, phi, and n.
- separate into public/private keys.

"""

# Note: Execute each step one by one.
p, q = Setup.pickInitialPrimes()
print "p: " + str(p)
print "q: " + str(q)

N = Algorithms.calcModulus(p, q)
print "N: " + str(N)

phi = Algorithms.calcEulersTotient(p, q)
print "phi: " + str(phi)

e = Setup.pickPublicExponent(phi)
print "e: " + str(e)

sub_1, mult_sub_1, sub_2, mult_sub_2 = Setup.calcSecretExponent(e, phi)
d = mult_sub_1
if(e == sub_2):
    d = mult_sub_2

print "sub_1: " + str(sub_1)
print "mult_sub_1: " + str(mult_sub_1)
print "sub_2: " + str(sub_2)
print "mult_sub_2: " + str(mult_sub_2)
print "d: " + str(d)


"""
Messaging: 
- add messages to queue
- encrypt each message as they come in
- decrypt message if there are messages available

"""
encrypted_messages = []
while True:
    choice = raw_input("Type 'message' to add a message, \
                             'decrypt' to decrypt the next message, or \
                             'exit' to stop interacting.")  
    if(choice == "message"):
        m = raw_input("Enter a message: ")
        m_encrypt = Message.encryptMessage(m)
        encrypted_messages.append(m_encrypt)
        print "Raw message: " + m
        print "Encrypted message: " + m_encrypt
    else if(choice == "decrypt"):
        if(len(encrypted_messages) == 0):
            print "Message queue is empty."
        else:
            m_encrypt = encrypted_messages.pop(0)
            m_decrypt = Message.decryptMessage(m_encrypt)

            print "Encrypted message: " + m_encrypt
            print "Decrypted message: " + m_decrypt 
    else if(choice == "exit"):
        break;
    else:
        print "Please type one of the specified options."
