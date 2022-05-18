
from collections import Counter
N, K = map(int, input().split())
S = list(input())
F = []
i = 1
while i*i <= N:
    d, r = divmod(N, i)
    if r == 0:
        F.append(i)
        if d != i:
            F.append(d)
    i += 1
F.sort()

def cnt(n):
    fans = 0
    for i in range(0, n):
        # print(n, S[i::n])
        c = Counter(S[i::n]).most_common()
        fans += N//n - c[0][1]
    return fans

for f in F:
    if cnt(f) <= K:
        print(f)
        exit()