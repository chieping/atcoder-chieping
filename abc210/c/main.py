from collections import defaultdict

N, K = map(int, input().split())
C = list(map(int, input().split()))

M = defaultdict(int)

for i in range(K):
    M[C[i]] += 1

ans = len(M)

for i in range(K, N):
    M[C[i]] += 1
    M[C[i-K]] -= 1
    if M[C[i-K]] == 0:
        M.pop(C[i-K])
    ans = max(ans, len(M))

print(ans)
