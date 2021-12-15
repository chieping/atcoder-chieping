from collections import defaultdict
import itertools

H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]

ans = 0
for bits in itertools.product((0, 1), repeat=H):
    rows = [x for x, bit in zip(P, bits) if bit == 1]
    m = defaultdict(int)
    for j in range(W):
        s = set()
        for i in range(len(rows)):
            s.add(rows[i][j])
        if len(s) == 1:
            n = s.pop()
            m[n] += len(rows)
            ans = max(ans, m[n])

print(ans)
