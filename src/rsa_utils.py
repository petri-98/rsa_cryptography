import random

from .math_utils import euclidean_algo, extended_GCD, fast_power, find_prime


def generate_RSA_Key(b):
    p = find_prime(2**(b-1),2**b - 1)
    q = find_prime(2**(b-1),2**b - 1)
    
    e = 2
    while euclidean_algo(e, (p-1)*(q-1)) != 1:
        e = random.randrange(2, (p-1)*(q-1) - 1)
        
    g = euclidean_algo(p-1,q-1)
    m = (p-1)*(q-1)//g
    d = extended_GCD(e,m)[1] % m
    
    PublicKey = [p*q, e]
    PrivateKey = [p*q, d]
    
    return [PublicKey, PrivateKey]

def RSA_encrypt(message, PublicKey):
    return fast_power(message,PublicKey[1],PublicKey[0])

def RSA_decrypt(cipher, PrivateKey):
    return fast_power(cipher,PrivateKey[1],PrivateKey[0])
