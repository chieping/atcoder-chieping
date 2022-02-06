import sys
readline = sys.stdin.readline
N, K = map(int, readline().split())
MOD = 10**9+7
ans = 0
top = 0
bottom = 0
for i in range(N+1):
    bottom += i
    top += N-i
    if i+1 < K:
        continue
    ans += top - bottom + 1
    ans %= MOD
print(ans)
