from collections import deque
import sys
readline = sys.stdin.readline
a, N = map(int, readline().split())

dijit = 1
n = N
while n >= 10:
    n //= 10
    dijit += 1
max_ = (10**dijit+1)
d = [-1] * max_
d[1] = 0

q = deque()
q.append(1)

while len(q) > 0:
    n = q.popleft()
    x = n*a
    if x <= max_ and d[x] == -1:
        d[x] = d[n] + 1
        q.append(x)
    if n >= 10 and n % 10 != 0:
        y = str(n)
        y = int(y[-1] + y[:-1])
        if d[y] == -1:
            d[y] = d[n] + 1
            q.append(y)
print(d[N])
