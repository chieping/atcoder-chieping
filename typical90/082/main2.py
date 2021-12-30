L, R = map(int, input().split())
MOD = 10**9+7

def count(n):
    if n == 0:
        return 0
    length = len(str(n))
    start = 10**(length-1)
    end = n
    res = (start+end)*(end-start+1)//2*length
    res %= MOD
    return res + count(start-1)

print((count(R)-count(L-1))%MOD)


