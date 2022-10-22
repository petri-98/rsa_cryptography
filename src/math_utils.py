import random


def euclidean_algo(a, b):
    if a % b == 0:
        return b
    return euclidean_algo(b, a % b)


def extended_GCD(a, b):
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
    return [g, u, v]


def fast_power(g, A, N):
    a = g
    b = 1
    while A > 0:
        if A % 2 == 1:
            b = b * a % N
        A = A // 2
        a = a * a % N
    return b


def find_root(c, e, p, q):
    if euclidean_algo(e, (p - 1) * (q - 1)) == 1:
        m = (p - 1) * (q - 1) / euclidean_algo(p - 1, q - 1)
        d = extended_GCD(e, m)[1] % m
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
    if (n % 2 == 0 or 1 < euclidean_algo(a, n) < n):
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


def find_prime(lowerBound, upperBound):
    n = random.randrange(lowerBound, upperBound)
    while not probably_prime(n):
        n = random.randrange(lowerBound, upperBound)
        if probably_prime(n) == True:
            return n
    return n
