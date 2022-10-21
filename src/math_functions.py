import random

def euclidean_algo(a,b):
    if a % b == 0:
        return b
    return euclidean_algo(b, a % b)

def extendedGCD(a,b):
    u = 1
    g = a
    x = 0
    y = b
    while y > 0:
        q,t = g//y, g%y
        s = u - q*x
        u, g = x, y
        x, y = s, t
    v = (g - a*u)//b
    return [g,u,v]

def fastPowerSmall(g,A,N):
    a = g
    b = 1
    while A>0:
        if A % 2 == 1:
            b = b * a % N
        A = A//2
        a = a*a % N
    return b

def findRoot5(c,e,p,q):
    if euclidean_algo(e,(p-1)*(q-1)) == 1:
        m = (p-1)*(q-1)/euclidean_algo(p-1,q-1)
        d = extendedGCD(e,m)[1] % m
        return fastPowerSmall(c,d,p*q)
    else:
        raise Exception("Error: e and (p-1)*(q-1) must be coprimes")

def pow2_times_odd(m):
    k = 0
    while m%2 == 0:
        k += 1
        m //= 2
    return k,m

def millerRabin(a, n):
    if (n%2 == 0 or 1 < euclidean_algo(a,n) < n):
        return True
    k, q = pow2_times_odd(n-1)
    a = fastPowerSmall(a,q,n)
        
    if a % n == 1:
        return False
        
    for _ in range(k):
        if a % n == n-1:
            return False
        a = a*a % n
    return True

def probablyPrime(n):
    for _ in range(20):
        a = random.randrange(2, n)
        if millerRabin(int(a),n) == True:
            return False
    return True

def findPrime(lowerBound, upperBound):
    n = random.randrange(lowerBound, upperBound)
    while not probablyPrime(n):
        n = random.randrange(lowerBound, upperBound)
        if probablyPrime(n) == True:
            return n
    return n
