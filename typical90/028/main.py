from collections import defaultdict
N = int(input())
n = 1010
B = [[0] * n for i in range(n)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    rx -= 1
    ry -= 1
    B[lx][ly] += 1
    B[rx+1][ly] -= 1
    B[lx][ry+1] -= 1
    B[rx+1][ry+1] += 1

for i in range(n):
    for j in range(1, n):
        B[i][j] = B[i][j-1] + B[i][j]

for j in range(n):
    for i in range(1, n):
        B[i][j] = B[i-1][j] + B[i][j]

ans = defaultdict(int)

for i in range(n):
    for j in range(n):
        ans[B[i][j]] += 1

for i in range(1, N+1):
    print(ans[i])
