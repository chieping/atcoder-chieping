import sys
readline = sys.stdin.readline
n, a, b = map(int, readline().split())
MOD = 10**9+7
ans = pow(2, n, MOD) - 1

def fact(k, n):
    ret = 1
    for i in range(k, n+1):
        ret = (ret * i) % MOD
    return ret

def c(n, k):
    inv = pow(fact(1, n-k), MOD-2, MOD)
    return fact(k+1, n)*inv%MOD

# 制約より、 1≤a<b≤min(n, 2 * 10^5) とあり
# c(n, a)の第2引数の代わりに n-a を渡すと計算量が減りTLEしなくなる
ans -= c(n, n-a)
ans -= c(n, n-b)
ans %= MOD
print(ans)
