def prime_table(n):
    global is_prime
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def osa_k(N):
    divisors = [0]*(N+1)
    for i in range(2, N+1):
        if divisors[i]:
            continue
        for j in range(i, N+1, i):
            if not divisors[j]:
                divisors[j] = i
    return divisors


print(osa_k(20))


def prime_factors(n):
    dic = {}
    cur = n
    for i in range(2, (int(n**0.5)+2)):
        if cur % i == 0:
            count = 0
            while cur % i == 0:
                count += 1
                cur //= i
            dic[i] = count
            if cur == 1:
                break
    if cur != 1:
        dic[cur] = 1
    return dic

# https://qiita.com/Kiri8128/items/eca965fe86ea5f4cbb98


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def isPrimeMR(n):
    assert 0 < n < 2**64
    if n == 1:
        return 0
    d = n - 1
    d = d // (d & -d)
    L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in L:
        if n == a:
            return 1
        t = d
        y = pow(a, t, n)
        if y == 1:
            continue
        while y != n - 1:
            y = (y * y) % n
            if y == 1 or t == n - 1:
                return 0
            t <<= 1
    return 1


def findFactorRho(n):
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):
        def f(x): return (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if isPrimeMR(g):
                return g
            elif isPrimeMR(n // g):
                return n // g
            return findFactorRho(g)


def primeFactor(n):
    i = 2
    ret = {}
    rhoFlg = 0
    while i*i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k:
            ret[i] = k
        i += 1 + i % 2
        if i == 101 and n >= 2 ** 20:
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k

    if n > 1:
        ret[n] = 1
    if rhoFlg:
        ret = {x: ret[x] for x in sorted(ret)}
    return ret
