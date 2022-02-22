import sys
readline = sys.stdin.readline
N, M = map(int, readline().split())
PS = []
for _ in range(M):
    p, s = readline().split()
    PS.append((int(p)-1, s))

ACed = [False] * N
pena = [0] * N
ans_pena = 0

for p, s in PS:
    if ACed[p]:
        continue
    if s == 'AC':
        ACed[p] = True
        ans_pena += pena[p]
    elif s == 'WA':
        pena[p] += 1

print(sum(ACed), ans_pena)