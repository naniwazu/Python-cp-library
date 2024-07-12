def inv_gcd(a, b):
    a %= b
    if a == 0:
        return (b, 0)
    s = b
    t = a
    m0 = 0
    m1 = 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        tmp = s
        s = t
        t = tmp
        tmp = m0
        m0 = m1
        m1 = tmp
    if m0 < 0:
        m0 += b // s
    return (s, m0)


def crt(r, m):
    assert len(r) == len(m)
    n = len(r)
    r0 = 0
    m0 = 1
    for i in range(n):
        assert 1 <= m[i]
        r1 = r[i] % m[i]
        m1 = m[i]
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return (0, 0)
            continue
        g, im = inv_gcd(m0, m1)
        u1 = m1 // g
        if (r1-r0) % g:
            return (0, 0)
        x = (r1-r0) // g * im % u1
        r0 += x * m0
        m0 *= u1
        if r0 < 0:
            r0 += m0
    return (r0, m0)
