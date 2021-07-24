N, K = map(int, input().split())

A = [list(map(int, input().split())) for i in range(N)]

ans = 10 ** 100

for i in range(N-K+1):
    for j in range(i, i+K):
        A[j][j]
