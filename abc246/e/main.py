# TLE
from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = [a-1 for a in A]
B = [b-1 for b in B]
INF = 10**18
dxs = [-1, -1, 1, 1]
dys = [1, -1, -1, 1]

board = [list(input()[:-1]) for _ in range(N)]
dist = [[INF] * N for _ in range(N)]

dist[A[0]][A[1]] = 0

q = deque()
q.append(A)

while len(q):
    i, j = q.popleft()
    cnt = dist[i][j]
    for dx, dy in zip(dxs, dys):
        ci = i
        cj = j
        while 0 <= ci < N and 0 <= cj < N and board[ci][cj] != '#':
            if cnt + 1 < dist[ci][cj]:
                dist[ci][cj] = cnt+1
                q.append((ci, cj))
            ci += dx
            cj += dy

if dist[B[0]][B[1]] == INF:
    print(-1)
else:
    print(dist[B[0]][B[1]])
