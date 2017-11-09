import Algorithms

"""
This module provides helper functions for RSA setup.

"""

# Function to ask user for initial primes p and q.
def pickInitialPrimes():
    picks = []
    print "Please choose 2 initial prime numbers."
    while(len(picks) < 2):
        num = input("Enter an initial prime number: ")
        isPrime = Algorithms.isPrime(num)
        message = ""
        if(isPrime):
            picks.append(num)
            message = str(num) + " is a prime number."
        else:
            message = str(num) + " is not a prime number."
        print message
    
    return picks[0], picks[1]

# Function to ask user for the public exponent.
def pickPublicExponent(phi):
    # do a while loop.
    while(True):
        num = input("Enter your public exponent: ")
        isBtwn = (1 < num) & (num < phi)
        isCoPrime = Algorithms.isCoPrime(num, phi)
        if(isBtwn & isCoPrime):
            print str(num) + " is a valid public exponent."
            return num
        else:
            print str(num) + " is not a valid public exponent. Try again"

"""
# Function to calculate the secret exponent.
def calcSecretExponent(e, phi):
    # compute: e * d congr 1 (mod phi)

    # just do Euclidean, then go backwards 

    # return result.
"""

