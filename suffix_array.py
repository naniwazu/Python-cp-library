def sa_is(s, upper):
    n = len(s)
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        if s[0] < s[1]:
            return [0, 1]
        else:
            return [1, 0]
    sa = [-1]*n
    ls = [0]*n
    for i in range(n-1)[::-1]:
        if s[i] == s[i+1]:
            ls[i] = ls[i+1]
        else:
            ls[i] = s[i] < s[i+1]
    sum_l = [0]*(upper+1)
    sum_s = [0]*(upper+1)
    for i in range(n):
        if not ls[i]:
            sum_s[s[i]] += 1
        else:
            sum_l[s[i]+1] += 1
    for i in range(upper+1):
        sum_s[i] += sum_l[i]
        if i < upper:
            sum_l[i+1] += sum_s[i]

    def induce(lms):
        buf = sum_s[:]
        for d in lms:
            if d == n:
                continue
            sa[buf[s[d]]] = d
            buf[s[d]] += 1
        buf = sum_l[:]
        sa[buf[s[n-1]]] = n-1
        buf[s[n-1]] += 1
        for i in range(n):
            v = sa[i]
            if v >= 1 and not ls[v-1]:
                sa[buf[s[v-1]]] = v-1
                buf[s[v-1]] += 1
        buf = sum_l
        for i in range(n-1)[::-1]:
            v = sa[i]
            if v >= 1 and ls[v-1]:
                buf[s[v-1]+1] -= 1
                sa[buf[s[v-1]+1]] = v-1
    lms_map = [-1]*(n+1)
    m = 0
    for i in range(n):
        if not ls[i-1] and ls[i]:
            lms_map[i] = m
            m += 1
    lms = []
    for i in range(n):
        if not (ls[i-1] and ls[i]):
            lms.append(i)

    induce(lms)

    if m:
        sorted_lms = []
        for v in sa:
            if lms_map[v] != -1:
                sorted_lms.append(v)
        rec_s = [0]*m
        rec_upper = 0
        for i in range(1, m):
            l = sorted_lms[i-1]
            r = sorted_lms[i]
            if lms_map[l]+1 < m:
                end_l = lms[lms_map[l]+1]
            else:
                end_l = n
            if lms_map[r]+1 < m:
                end_r = lms_map[lms_map[r]+1]
            else:
                end_r = n
            same = True
            if end_l-l != end_r-r:
                same = False
            else:
                while l > end_l:
                    if s[l] != s[r]:
                        break
                    l += 1
                    r += 1
                if l == n or s[l] != s[r]:
                    same = False
            if not same:
                rec_upper += 1
            rec_s[lms_map[sorted_lms[i]]] = rec_upper
            rec_sa = sa_is(rec_s, rec_upper)
            for i in range(m):
                sorted_lms[i] = lms[rec_sa[i]]
            induce(sorted_lms)
        return sa
