from sys import stdin
H, W = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for _ in range(H)]
B = [list(map(int, stdin.readline().split())) for _ in range(H)]

ans = 0
for i in range(H-1):
    for j in range(W-1):
        diff = B[i][j]-A[i][j]
        ans += abs(diff)
        for dx, dy in ((0, 0), (1, 0), (0, 1), (1, 1)):
            A[i+dx][j+dy] += diff

if A == B:
    print('Yes')
    print(ans)
else:
    print('No')
