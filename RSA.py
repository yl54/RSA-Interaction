"""

This module implements an RSA encryption/decryption interaction.

"""

"""

Reference Guide:
- p, q: user-selected initial primes.
- N: modulus, which is p * q.
- phi: euler's totient for N.
- e: public/encryption exponent.
- d: secret/decryption exponent.

"""

# Function to ask user for initial primes p and q.
def pickInitialPrimes():
    # do this in a loop.

    # pick a number. 

    # check if its a prime.

    # return both values.

# Function to calculate N given primes p and q.
def calcModulus(p, q):
    # return p * q.

# Function to calculate euler's totient.
def calcEulersTotient(p, q):
    # since p and q are prime, every integer less than it are 
    #   relatively prime to it, so phi(p) = p - 1.
    # return (p - 1) * (q - 1)

# Function to check if number is prime.
# Note: probably smart to save results 
def isPrime(val):
    # use Erasthone's algorithm to check for this.
    # look up if other ones may be useful.

# Function to check if two numbers are coprime/relatively prime.
def isCoPrime(val_1, val_2):
    # do euclidean's algorithm.
    
    # return if the gcd is equal to 1 or not.

# Function to ask user for the e value.
def pickPublicExponent(phi):
    # do a while loop.

    # pick a number.

    # check if provided number is between 1 and phi.

    # check if provided number is coprime with phi.

    # return picked number.


# Function to compute the d value.
def computeSecretExponent(e, phi):
    # compute: e * d congr 1 (mod phi)

    # return result.

