import heapq
import math
from pprint import pprint
import sys
readline = sys.stdin.readline
a, N = map(int, readline().split())

dijit = 1
n = N
while n >= 10:
    n //= 10
    dijit += 1

dp = [False] * (10**dijit+2)
m = (10**dijit+1)
dp[1] = True

h = []

heapq.heappush(h, (1, 0))

while len(h) > 0:
    n, cnt = heapq.heappop(h)
    if n == N:
        print(cnt)
        exit()
    x = n*a
    if x <= m and not dp[x]:
        dp[x] = True
        heapq.heappush(h, (x, cnt+1))
    if n >= 10 and n % 10 != 0:
        y = str(n)
        y = int(y[-1] + y[1:-1] + y[0])
        if not dp[y]:
            dp[y] = True
            heapq.heappush(h, (y, cnt+1))
print(-1)


    
    


# for i in range(2, 10**dijit+1):
#     d, m = divmod(i, a)
#     if m == 0:
#         dp[i] = min(dp[i], dp[d] + 1)
#     if i >= 10:
#         n  = str(i)

#         n = int(n[-1] + n[1:-1] + n[0])
#         dp[i] = min(dp[i], dp[n] + 1)
#     if dp[N] != INF:
#         print(dp[N])
#         exit()


