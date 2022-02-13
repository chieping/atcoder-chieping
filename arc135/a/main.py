from functools import lru_cache
X = int(input())
MOD = 998244353

@lru_cache
def dfs(x, ans):
    if x > 3:
        if x % 2 == 0:
            res = dfs(x//2, 1)
            res *= res
            res %= MOD
            ans *= res
            ans %= MOD
            return ans
        else:
            a = x // 2
            b = x // 2 + 1
            res = dfs(a, 1)
            res *= dfs(b, 1)
            ans *= res
            ans %= MOD
            return ans
    else:
        ans *= x
        ans %= MOD
        return ans

print(dfs(X, 1))