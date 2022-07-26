H, W, N = map(int, input().split())
A = [list(map(lambda x: int(x)-1, input().split())) for _ in range(H)]
C = list(map(int, input().split()))
edge = [[] for _ in range(N)]
DX = [-1, 0, 1, 0]
DY = [0, -1, 0, 1]
for i in range(H):
    for j in range(W):
        for dx, dy in zip(DX, DY):
            if not (0 <= i+dx < H and 0 <= j+dy < W):
                continue
            if A[i][j] == A[i+dx][j+dy]:
                continue
            if A[i+dx][j+dy] not in edge[A[i][j]]:
                edge[A[i][j]].append(A[i+dx][j+dy])
                edge[A[i+dx][j+dy]].append(A[i][j])

# print(*edge, sep='\n')
ans = True
for a in range(N):
    for b in edge[a]:
        if C[a] == C[b]:
            print('No')
            exit()
print('Yes')