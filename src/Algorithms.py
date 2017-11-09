"""
This module provides helper functions for mathematical computations.

"""

# Function to calculate N given primes p and q.
def calcModulus(p, q):
    return p * q

# Function to calculate euler's totient.
def calcEulersTotient(p, q):
    return (p - 1) * (q - 1)

# Function to check if number is prime.
# Note: probably smart to save results 
def isPrime(val):
    # can reuse these two at some point
    primes = [1]
    found_values = {1}

    iter = 2
    mult = 1
    while iter < val:
        if iter not in found_values:
            primes.append(iter)
            while mult < val:
                found_values.add(mult)
                mult += mult
        # move onto next number to look for
        iter += 1

    return val not in found_values

# Function to check if two numbers are coprime/relatively prime.
def isCoPrime(val_1, val_2):
    dividends, quotients = calcEuclid(val_1, val_2)
    return dividends[len(dividends) - 1] == 1

# Function to execute the euclidean algorithm on two numbers.
def calcEuclid(val_1, val_2):
    # identify which number is smaller.
    dividend = max(val_1, val_2)
    divisor = min(val_1, val_2)
    dividends = [dividend, divisor]
    quotients = []
    while (dividend != 0 && divisor != 0): 
        quotient, remainder = calcDivision(dividend, divisor)
        dividends.append(remainder)
        quotients.append(quotient)
        divisor = quotient
        dividend = divisor
    return dividends, quotients

# Function to execute the extended euclidean algorithm.
def calcExtendEclid(dividends, quotients):
    div_length = len(dividends)
    quo_length = len(quotients)
    gcd = dividends[div_length - 1]
    sub_1 = dividends[div_length - 2]
    sub_2 = dividends[div_length - 3]
    mult_sub_1 = quotients[quo_length - 2]
    mult_sub_2 = 1
    int count = 0
    for i in xrange(div_length - 4, 0, -1):
        div = dividends[i]
        quo = quotients[i - 1]
        sub_1, mult_sub_1, sub_2, mult_sub_2 = substitute(sub_1, mult_sub_1, sub_2, mult_sub_2, div, quo)
        count++

    return sub_1, mult_sub_1, sub_2, mult_sub_2

# Function to handle substitutions during extended Euclidean algorithm.
def substitute(sub_1, mult_sub_1, sub_2, mult_sub_2, sub_3, quo):
    low_val, low_mult, high_val, high_mult = assign(sub_1, mult_sub_1, sub_2, mult_sub_2)
    new_high_mult = high_mult + (quo * low_mult)
    return sub_3, low_mult, high_val, new_high_mult

# Function to help assign lower/higher values.
def assign(sub_1, mult_sub_1, sub_2, mult_sub_2)
    if sub_2 > sub_1: 
        return sub_1, mult_sub_1, sub_2, mult_sub_2
    else:
        return sub_2, mult_sub_2, sub_1, mult_sub_1'

# Function to execute division algorithm and get the quotient and remainder.
def calcDivision(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend - (divisor * quotient)
    return quotient, remainder


# Probably wise to have an object that stores previous results of 
#   algorithm if its gonna be a big number.
# First, do the way without storage.


