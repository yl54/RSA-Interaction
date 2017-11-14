import Algorithms
import Message
import Setup

"""
This module does tests on some of the functions to see
  if they are working properly or not. 

"""

# Test the prime function.

# Test the coprime function.

# Test the Euclidean Algorithm.

# Test the Extended Euclidean Algorithm.


# Test the successive squaring mod algorithm.
"""
a = 7
b = 327
n = 853
print "a: " + str(a)
print "b: " + str(b)
print "n: " + str(n)
result = Algorithms.calcLargeMod(a, b, n)
print "result: "  + str(result)
"""

# Test the encryption of a message.
ref_ch_to_int, ref_int_to_ch = Message.assignChCodes()
N = 90024247
e = 2706925

# Note: make a function to figure out what the prime factors are.
phi = Algorithms.calcEulersTotient(9109, 9883)
sub_1, mult_sub_1, sub_2, mult_sub_2 = Setup.calcSecretExponent(e, phi)
d = mult_sub_1
if(e == sub_2):
    d = mult_sub_2

encry_result = Message.encryptMessage("i love math", N, e, ref_ch_to_int)
print "encry_result: " + str(encry_result)

# Test the decryption of a message.
decry_result = Message.decryptMessage(encry_result, N, d, ref_int_to_ch)
print "decry_result: " + decry_result

#m_encrypt_A = 84069637
#m_encrypt_B = 84066637
#result = Message.decryptMessage(m_encrypt_B, N, d, ref_int_to_ch)
#print "result: "  + str(result)
