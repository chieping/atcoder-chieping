import sys
readline = sys.stdin.readline
N, M = map(int, readline().split())
SC = [list(map(int, readline().split())) for _ in range(M)]

for i in range(1000):
    S = str(i)
    if len(S) != N:
        continue
    ok = True
    for s, c in SC:
        if s-1 < len(S):
            if int(S[s-1]) != c:
                ok = False
        else:
            ok = False
    if ok:
        print(i)
        exit()
print(-1)
