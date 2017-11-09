"""
This module provides helper functions for mathematical computations.

"""

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

# Function to execute the euclidean algorithm on two numbers.
def calcEuclid(val_1, val_2):
    # do while loop until gcd remainder is 0
        # identify which number is smaller.

        # use division algorithm.

        # change variables around.

        # store each of these iterations.

    # return the g.c.d and iterations.


# Function to execute the extended euclidean algorithm.
def calcExtendEclid(result, iters):
    # do while loop until iterations get to beginning
        # get the next number in the iteration.

        # find the number that fits the amount.

        # change variables around

    # return the multipliers 

# Function to execute division algorithm and get the quotient and remainder.
def calcDivision(dividend, divisor):
    # get quotient and remainder


# Probably wise to have an object that stores previous results of 
#   algorithm if its gonna be a big number.
# First, do the way without storage.


