N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    ans += sum(A[i][j] * B[j] for j in range(M)) + C > 0
print(ans)