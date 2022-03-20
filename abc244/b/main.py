import sys
input = sys.stdin.readline
N = int(input())
T = list(input()[:-1])
now = [0, 0]
dil = [(1, 0), (0, -1), (-1, 0), (0, 1)]
di = 0
for c in T:
    if c == 'S':
        now[0] += dil[di][0]
        now[1] += dil[di][1]
    else:
        di = (di + 1) % 4
print(*now)
