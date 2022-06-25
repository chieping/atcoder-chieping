N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
M = [False] * (N+1)
for a in A:
    M[a] = True

for i in range(Q):
    l = L[i]
    a = A[l-1]
    if a+1 <= N and not M[a+1]:
        M[a] = False
        M[a+1] = True
        A[l-1] += 1

ans = []
for i, m in enumerate(M[1:], 1):
    if m:
        ans.append(i)
print(*ans)
