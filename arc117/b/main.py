N = int(input())
A = list(map(int, input().split()))
MOD = 10**9+7
A.sort(reverse=True)
A.append(0)
ans = 1
cur = A[0]
for a in A:
    if a < cur:
        ans *= cur-a+1
        ans %= MOD
        cur = a
print(ans)