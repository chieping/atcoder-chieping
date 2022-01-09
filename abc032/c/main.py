from pprint import pprint
import sys
readline = sys.stdin.readline
N, K = map(int, readline().split())
S = [int(readline()) for _ in range(N)]

# 0が1つでも存在すれば答えはNになる
if 0 in S:
    print(N)
    exit()

ans = 0
r = 0
tmp = 1
for l in range(N):
    while r < N and tmp * S[r] <= K:
        tmp *= S[r]
        r += 1
    ans = max(ans, r-l)
    if l == r:
        r += 1
    else:
        tmp //= S[l]
 
print(ans)
