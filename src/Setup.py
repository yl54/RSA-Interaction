"""

This module provides helper functions for RSA setup.

"""

# Function to ask user for initial primes p and q.
def pickInitialPrimes():
    # do this in a loop.

    # pick a number. 

    # check if its a prime.

    # return both values.

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


