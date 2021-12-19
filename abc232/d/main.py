H, W = map(int, input().split())
C = [list(input())for _ in range(H)]
D = [[0] * (W+1) for _ in range(H+1)]
for i in range(H-1, -1, -1):
    for j in range(W-1, -1, -1):
        if C[i][j] == '#': continue
        D[i][j] = max(D[i+1][j], D[i][j+1]) + 1
print(D[i][j])
