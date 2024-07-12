from heapq import heappush, heappushpop


class slope_trick:  # 傾きが整数の区分線形凸関数を管理する、定数関数f(x)=0で初期化される
    def __init__(self):
        INF = 10**18
        self._min = 0
        self._L = [INF]
        self._R = [INF]

    def min(self):  # 最小値、及び最小値を取る区間を返す
        return (self._min, -self._L[0], self._R[0])

    def add(self, a):  # 定数関数x=aを加算する
        self._min += a

    def add_rampR(self, a):  # max(x-a, 0)を加算する
        l_0 = -self._L[0]
        self._min += max(l_0-a, 0)
        heappush(self._R, -heappushpop(self._L, -a))

    def add_rampL(self, a):  # max(a-x, 0)を加算する
        r_0 = self._R[0]
        self._min += max(a-r_0, 0)
        heappush(self._L, -heappushpop(self._R, a))
