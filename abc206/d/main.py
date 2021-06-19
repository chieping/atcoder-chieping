from collections import deque
import sys
sys.setrecursionlimit(100000000)

N = int(input())
A = list(map(int, input().split()))

def replace(nn, n1, n2):
    for i in range(len(nn)):
        if nn[i] == n1:
            nn[i] = n2
    return nn

Q = deque()
Q.append(A)
ans = 0

while len(Q) > 0:
    a = Q.popleft()

    if len(a) <= 1:
        break
    if a[0] == a[-1]:
        Q.append(a[1:-1])
    else:
        ans += 1
        Q.append(replace(a[1:-1], a[0], a[-1]))
        Q.append(replace(a[1:-1], a[-1], a[0]))
        
print(ans)
