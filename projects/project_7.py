def comb(n, k):
    res = 1

    if k > n:
        res = 0
    else:
        k = min(k, n - k)

        for i in range(k):
            res = res * (n - i) // (i + 1)

    return res


print(comb(10,4))