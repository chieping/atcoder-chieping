N = int(input())
n = 1001
B = [[0] * n for i in range(n)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    B[lx][ly] += 1
    B[rx][ly] -= 1
    B[lx][ry] -= 1
    B[rx][ry] += 1

for i in range(n):
    for j in range(1, n):
        B[i][j] += B[i][j-1]

for i in range(1, n):
    for j in range(n):
        B[i][j] += B[i-1][j]

ans = [0] * (N+1)

for i in range(n):
    for j in range(n):
        ans[B[i][j]] += 1

for i in range(1, N+1):
    print(ans[i])
