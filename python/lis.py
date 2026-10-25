import bisect


def lis(seq):  # 狭義単調増加な部分列の最長の長さ
    tails = []
    for x in seq:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
