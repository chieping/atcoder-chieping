from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
INF = 10**9
dxs = [-1, -1, 1, 1]
dys = [1, -1, -1, 1]
board = []
board.append(['#'] * (N+2))
for _ in range(N):
    board.append(['#'] + list(input()[:-1]) + ['#'])
board.append(['#'] * (N+2))
dist = [[INF] * (N+2) for _ in range(N+2)]
dist[A[0]][A[1]] = 0
q = deque()
q.append(A)

while len(q):
    i, j = q.popleft()
    cnt = dist[i][j]
    for dx, dy in zip(dxs, dys):
        ci = i + dx
        cj = j + dy
        while board[ci][cj] != '#' and dist[ci][cj] > dist[i][j]:
            if cnt + 1 < dist[ci][cj]:
                dist[ci][cj] = cnt+1
                q.append((ci, cj))
            ci += dx
            cj += dy

ans = dist[B[0]][B[1]]
print(ans if ans != INF else -1)
