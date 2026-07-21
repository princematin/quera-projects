
def comb(n, k):
    ans = n - k
    ans = ans * k
    ans = n / ans
    return ans