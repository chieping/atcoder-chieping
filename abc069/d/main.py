from collections import deque
H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))
ans = [[0] * W for _ in range(H)]
que = deque()
for i, a in enumerate(A, 1):
    for _ in range(a):
        que.append(i)

for i in range(H):
    if i % 2:
        R = range(W)
    else:
        R = range(W-1, -1, -1)
    for j in R:
        ans[i][j] = que.popleft()

for i in range(H):
    print(*ans[i])