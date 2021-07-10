N = int(input())
C = list(map(int, input().split()))

C.sort()

MOD = 10**9+7

ans = 1

for i in range(N):
    ans = (ans * max(0, C[i]-i)) % MOD

print(ans)
