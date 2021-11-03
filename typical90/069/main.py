N, K = map(int, input().split())
MOD = 10**9+7

# while loop版
# def solve(x, n):
#     ans = 1
#     while n:
#         if n % 2:
#             ans *= x
#             ans %= MOD
#         x *= x
#         x %= MOD
#         n >>= 1
#     return ans

def solve(x, n):
    if n == 0:
        return 1
    elif n % 2:
        return x * solve(x, n-1) % MOD
    else:
        a = solve(x, n//2) % MOD
        return a**2 % MOD

if N == 1:
    print(K)
    exit()

print(K * (K-1) * solve(K-2, N-2) % MOD)
