from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
cnt = defaultdict(list)
for i in range(N):
    a = int(input())
    cnt[a].append(i)
ans = [0] * N

for i, (a, idxs) in enumerate(sorted(cnt.items())):
    for j in idxs:
        ans[j] = i
print(*ans, sep='\n')
