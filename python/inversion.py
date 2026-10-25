from BIT import BIT


def inversion(ls):
    encode = {e: i for i, e in enumerate(sorted(set(ls)))}
    compressed_ls = [encode[e] for e in ls]
    bit = BIT(len(encode))
    ret = 0
    for x in compressed_ls[::-1]:
        bit.update(x, 1)
        ret += bit.sum(0, x)
    return ret
