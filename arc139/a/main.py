from functools import lru_cache
N = int(input())
T = list(map(int, input().split()))
INF = 1<<100 - 1

@lru_cache(maxsize=None)
def ctz(n):
    fans = 0
    i = 0
    while not n&1<<i and 1<<i <= n:
        fans += 1
        i += 1
    return fans

last = 0
for cnt in T:
    now = max(last + 1, 1<<cnt)
    while ctz(now) != cnt:
        now = now >> cnt
        now += 1
        now = now << cnt
    last = now
print(last)