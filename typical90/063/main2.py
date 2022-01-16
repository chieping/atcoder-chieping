from collections import defaultdict
import itertools
import sys
readline = sys.stdin.readline
H, W = map(int, readline().split())
P = [list(map(int, readline().split())) for _ in range(H)]

ans = 0
for p in itertools.product((True, False), repeat=H):
    M = defaultdict(int)
    for j in range(W):
        same = True
        tmp = None
        for i, flag in enumerate(p):
            if not flag:
                continue
            if not tmp:
                tmp = P[i][j]
            else:
                if tmp != P[i][j]:
                    same = False
                    break
        if tmp and same:
            M[tmp] += 1
    if M.values():
        ans = max(ans, max(M.values())*sum(p))
print(ans)
