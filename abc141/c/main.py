N, K, Q = map(int, input().split())
ans = [0] * (N+1)
for _ in range(Q):
    ans[int(input())] += 1

for n in ans[1:]:
    if K - Q + n > 0:
        print('Yes')
    else:
        print('No')
