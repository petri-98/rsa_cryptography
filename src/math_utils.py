import random


#TODO add docstrings


def extended_gcd(a, b):
    u = 1
    g = a
    x = 0
    y = b
    while y > 0:
        q, t = g // y, g % y
        s = u - q * x
        u, g = x, y
        x, y = s, t
    v = (g - a * u) // b
    return g, u, v


def fast_power(g, l, n):
    a = g
    b = 1
    while l > 0:
        if l % 2 == 1:
            b = b * a % n
        l = l // 2
        a = a * a % n
    return b


def find_root(c, e, p, q):
    if extended_gcd(e, (p - 1) * (q - 1))[0] == 1:
        m = (p - 1) * (q - 1) / extended_gcd(p - 1, q - 1)[0]
        d = extended_gcd(e, m)[1] % m
        return fast_power(c, d, p * q)
    else:
        raise Exception("Error: e and (p-1)*(q-1) must be coprimes")


def count_powers_two(m):
    k = 0
    while m % 2 == 0:
        k += 1
        m //= 2
    return k, m


def miller_rabin(a, n):
    if (n % 2 == 0 or 1 < extended_gcd(a, n)[0] < n):
        return True
    k, q = count_powers_two(n - 1)
    a = fast_power(a, q, n)

    if a % n == 1:
        return False

    for _ in range(k):
        if a % n == n - 1:
            return False
        a = a * a % n
    return True


def probably_prime(n):
    for _ in range(20):
        a = random.randrange(2, n)
        if miller_rabin(int(a), n) == True:
            return False
    return True


def find_prime(lower_bound, upper_bound):
    n = random.randrange(lower_bound, upper_bound)
    while not probably_prime(n):
        n = random.randrange(lower_bound, upper_bound)
        if probably_prime(n) == True:
            return n
    return n
