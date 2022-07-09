from itertools import permutations
N, M = map(int, input().split())
GA = [[False] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    GA[a][b] = True
    GA[b][a] = True
GB = [[False] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    GB[a][b] = True
    GB[b][a] = True

for P in permutations(range(N)):
    G = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            G[i][j] = GA[P[i]][P[j]]
    if G == GB:
        print('Yes')
        exit()
print('No')
