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
    while iter < (val // 2 + 1):
        if iter not in found_values:
            primes.append(iter)
            total = 0
            while total <= val:
                found_values.add(total)
                total += iter
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
    print "dividend: " + str(dividend)
    print "divisor: " + str(divisor) 
    dividends = [dividend, divisor]
    quotients = []
    while (dividend != 1 and divisor != 1) and \
          (dividend != 0 and divisor != 0): 
        quotient, remainder = calcDivision(dividend, divisor)
        print "------------------------"
        print "quotient: " + str(quotient)
        print "remainder: " + str(remainder)
        print "------------------------"
        dividends.append(remainder)
        quotients.append(quotient)
        dividend = divisor
        divisor = remainder
    print "Euclidean Algorithm results: "
    print "dividends: " + ", ".join(str(x) for x in dividends)
    print "quotients: " + ", ".join(str(x) for x in quotients)
    return dividends, quotients

# Function to execute the extended euclidean algorithm.
# This function assumes that the Euclidean algorithm 
#   went through at least 4 iterations.
def calcExtendEuclid(dividends, quotients):
    div_length = len(dividends)
    quo_length = len(quotients)
    gcd = dividends[div_length - 1]
    sub_1 = dividends[div_length - 2]
    sub_2 = dividends[div_length - 3]
    mult_sub_1 = quotients[quo_length - 1]
    mult_sub_2 = 1
    count = 0
    for i in xrange(div_length - 4, -1, -1):
        div = dividends[i]
        quo = quotients[i]
        print "------------------------"
        print "sub_1: " + str(sub_1)
        print "mult_sub_1: " + str(mult_sub_1)
        print "sub_2: " + str(sub_2)
        print "mult_sub_2: " + str(mult_sub_2)
        print "div: " + str(div)
        print "quo: " + str(quo) 
        print "------------------------"
        sub_1, mult_sub_1, sub_2, mult_sub_2 = \
                    substitute(sub_1, mult_sub_1, sub_2, mult_sub_2, div, quo)
        count += 1
    print "------------------------"
    print "Extended Euclidean Algorithm results: "
    print ", ".join([str(sub_1), str(mult_sub_1), str(sub_2), str(mult_sub_2)])
    print "------------------------"
    return sub_1, mult_sub_1, sub_2, mult_sub_2

# Function to handle substitutions during extended Euclidean algorithm.
def substitute(sub_1, mult_sub_1, sub_2, mult_sub_2, sub_3, quo):
    low_val, low_mult, high_val, high_mult = \
                    assign(sub_1, mult_sub_1, sub_2, mult_sub_2)
    new_high_mult = high_mult + (quo * low_mult)
    return sub_3, low_mult, high_val, new_high_mult

# Function to help assign lower/higher values.
def assign(sub_1, mult_sub_1, sub_2, mult_sub_2):
    if(sub_2 > sub_1): 
        return sub_1, mult_sub_1, sub_2, mult_sub_2
    else:
        return sub_2, mult_sub_2, sub_1, mult_sub_1

# Function to execute division algorithm and get the quotient and remainder.
def calcDivision(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend - (divisor * quotient)
    return quotient, remainder

# Function to calculate mod problems with large integers.
#   These problems are of the form: t congr a^b mod n, return t.  
#   This particular method leverages successive squaring.
def calcLargeMod(a, b, n):
    # Retrieve all values of a^(2*x) mod n. While loop.
    # Do until 2*x is greater than b.
    current = a
    mod_nums = {}
    mod_nums[0] = current
    pwr = 1
    while 2^pwr < b:
        print "pwr: " + str(pwr)
        print "2 pwr: " + str(2^pwr)
        current = current^2 % n
        mod_nums.append(current)
        mod_nums[pwr] = current
        print "current: " + str(current)
        pwr += 1
    
    # Do loop to figure out which are the largest values 
    #   of 2 that add up to b. 
    # Do until 0 remainder. Will always get a 0 at some point.
    # Do from largest to smallest value of 2.
    # Can store this stuff in a dict. 
    # For each value that corresponds to power, do a mod n 
    #   with the multiplication. Keeps everything small.
    pwr -= 1
    diff = b
    mult = 1 # not sure if this is correct
    while (pwr > -1) and (diff > 0):
        # Check if this power of 2 is less than diff
        pwr_amt = 2^pwr
        print "pwr: " + str(pwr)
        print "pwr_amt: " + str(pwr_amt)
        print "diff: " + str(diff)
        if pwr_amt > diff:
            print "continue"
            pwr -= 1
            continue
        # Subtract from diff.
        diff -= pwr_amt
        print "diff - pwr_amt: " + str(diff)
        # Multiply result with the mod number associated 
        #   that power.
        print "mult: " + str(mult)
        mult *= mod_nums[pwr]
        # Mod the number by n.
        mult %= n
        print "(mult * mod_nums[pwr]) mod n: " + str(mult)
        pwr -= 1
        
    # Return the last modded value.
    return mult
