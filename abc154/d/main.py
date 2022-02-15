import sys
readline = sys.stdin.readline
N, K = map(int, readline().split())
P = list(map(int, readline().split()))
l = 0
r = 0
ans = 0
tmp = 0
while r < N:
    tmp += (P[r]+1)/2
    if r - l >= K:
        tmp -= (P[l]+1)/2
        l += 1
    r += 1
    ans = max(ans, tmp)
print(ans)
