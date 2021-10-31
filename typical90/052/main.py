N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
MOD = 10**9+7
ans = 1
for i in range(N):
    s = sum(A[i])
    ans *= s
    ans %= MOD
print(ans)
