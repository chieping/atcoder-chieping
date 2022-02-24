from itertools import product
import sys
readline = sys.stdin.readline
N = int(readline())
A = []
B = []
for i in range(N):
    a = int(readline())
    A.append(a)
    for _ in range(a):
        x, y = map(int, readline().split())
        x -= 1
        B.append((i, x, y))

ans = 0
for P in product([1, 0], repeat=N):
    for a, x, y in B:
        if P[a] == 1:
            if P[x] == 1 and y == 0:
                break
            elif P[x] == 0 and y == 1:
                break
    else:
        ans = max(ans, sum(P))
print(ans)