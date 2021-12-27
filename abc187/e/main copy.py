# TLE
# O(qn)なのでTLEするよね
from collections import deque
N = int(input())
A = [0]
B = [0]
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    edges[a].append(b)
    edges[b].append(a)

def solve(start, block, add):
    global C
    que = deque()
    visited = [False] * (N+1)
    que.append(start)
    visited[start] = True
    while len(que) > 0:
        a = que.pop()
        C[a] += add
        for edge in edges[a]:
            if not visited[edge] and edge != block:
                que.append(edge)
                visited[edge] = True

C = [0] * (N+1)
Q = int(input())
for _ in range(Q):
    t, e, x = map(int, input().split())
    if t == 1:
        solve(A[e], B[e], x)
    elif t == 2:
        solve(B[e], A[e], x)

print(*C[1:], sep="\n")
