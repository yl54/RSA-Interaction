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
- m: message.
- m_encry = encrypted message.
- m_decry = decrypted message.

"""



