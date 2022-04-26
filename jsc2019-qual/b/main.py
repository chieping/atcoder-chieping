N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9+7
ans1 = 0
ans2 = 0
for i, a in zip(range(N-1, -1, -1), A[::-1]):
    ans1 += sum(a < b for b in A[:i])
for a1 in A:
    ans2 += sum(a1 > a2 for a2 in A)
ans = 0
ans += ans1 * K % MOD
ans += ans2 * (K*(K-1)//2) % MOD
print(ans % MOD)