def Z_algorithm(S):
    l = len(S)
    A = [0]*l
    i = 1
    j = 0
    while i < l:
        while (i+j < l and S[j] == S[i+j]):
            j += 1
        A[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < l and k + A[k] < j:
            A[i+k] = A[k]
            k += 1
        i += k
        j -= k
    return A
