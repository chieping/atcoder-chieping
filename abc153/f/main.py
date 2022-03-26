from collections import deque
import sys
readline = sys.stdin.readline
N, D, A = map(int, input().split())
XH = [list(map(int, input().split())) for _ in range(N)]
XH.sort()
ans = 0
q = deque()
tot = 0
for x, h in XH:
    while len(q) and q[0][0] < x:
        tot -= q.popleft()[1]
    h -= tot
    if h > 0:
        n = (h+A-1)//A
        ans += n
        tot += n*A
        q.append((x+2*D, n*A))
print(ans)