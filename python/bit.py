class BIT:  # Binary Indexed Tree

    def __init__(self, n) -> None:
        self.n = n
        self.data = [0] * self.n

    def update(self, idx, x):
        assert 0 <= idx < self.n
        idx += 1
        while idx <= self.n:
            self.data[idx - 1] += x
            idx += idx & -idx

    def sum(self, l, r):
        assert 0 <= l <= r <= self.n
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s
