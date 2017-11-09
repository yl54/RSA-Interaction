import Algorithms
#import Message
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

p, q = Setup.pickInitialPrimes()
N = Algorithms.calcModulus(p, q)
phi = Algorithms.calcEulersTotient(p, q)
e = Setup.pickPublicExponent(phi)
d = Setup.calcSecretExponent(e, phi)

print "p: " + str(p)
print "q: " + str(q)
print "N: " + str(N)
print "phi: " + str(phi)
print "e: " + str(e)
print "d: " + str(d)

"""
Messaging: 

"""
