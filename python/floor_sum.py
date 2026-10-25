def floor_sum(n, m, a, b):
    res = 0
    while True:
        if a >= m:
            res += (a//m) * n * (n-1) // 2
            a %= m
        if b >= m:
            res += n * (b//m)
            b %= m
        if a*n + b < m:
            break
        u = (a*n + b)//m
        v = u*m - b
        res += (n - (v+a-1)//a) * u
        n, m, a, b = u, a, m, (a-v) % a
    return res
