from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

M = defaultdict(int)
ans = 0

for i in range(N):
    M[A[i] % 200] += 1

for k, v in M.items():
    ans += (v * (v-1)) // 2

print(ans)
