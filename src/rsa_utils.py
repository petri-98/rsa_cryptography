import random

from .math_utils import extended_gcd, fast_power, find_prime


# TODO add docstrings


def generate_rsa_key(b):
    p = find_prime(2**(b - 1), 2**b - 1)
    q = find_prime(2**(b - 1), 2**b - 1)

    e = 2
    while extended_gcd(e, (p - 1) * (q - 1))[0] != 1:
        e = random.randrange(2, (p - 1) * (q - 1) - 1)

    g = extended_gcd(p - 1, q - 1)[0]
    m = (p - 1) * (q - 1) // g
    d = extended_gcd(e, m)[1] % m

    public_key = [p * q, e]
    private_key = [p * q, d]

    return [public_key, private_key]


def rsa_encrypt(text, public_key):
    return fast_power(text, public_key[1], public_key[0])


def rsa_decrypt(text, private_key):
    return fast_power(text, private_key[1], private_key[0])
