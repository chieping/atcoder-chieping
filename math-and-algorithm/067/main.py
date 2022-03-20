H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Hsum = [sum(a) for a in A]
Wsum = [sum(a) for a in zip(*A)]
for i in range(H):
    print(*[Hsum[i] + Wsum[j] - A[i][j] for j in range(W)])
