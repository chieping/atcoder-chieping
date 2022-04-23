from collections import Counter
N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
M = max(A)
ans = 0
for q in range(1, M+1):
    r = 1
    while q*r <= M:
        ans += C[q] * C[r] * C[q*r]
        r += 1
print(ans)
