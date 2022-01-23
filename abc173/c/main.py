from itertools import product
import sys
readline = sys.stdin.readline

H, W, K = map(int, readline().split())
C = [readline()[:-1] for _ in range(H)]

ans = 0
for p1 in product([True, False], repeat=H):
    h = [i for i, p in enumerate(p1) if p]
    for p2 in product([True, False], repeat=W):
        w = [i for i, p in enumerate(p2) if p]
        black = 0
        for i in h:
            for j in w:
                black += C[i][j] == '#'
        ans += black == K

print(ans)
