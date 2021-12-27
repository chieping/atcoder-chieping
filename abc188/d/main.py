from collections import defaultdict
N, C = map(int, input().split())

M = defaultdict(int)

for _ in range(N):
    a, b, c = map(int, input().split())
    M[a] += c
    M[b+1] -= c
M[10**10] = 0

ans = 0
current_fee = 0
prev_day = 0
for current_day, value in sorted(M.items()):
    ans += min(C, current_fee) * (current_day-prev_day)
    current_fee += value
    prev_day = current_day
print(ans)
