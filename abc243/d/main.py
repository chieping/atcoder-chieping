from pprint import pprint
import sys
input = sys.stdin.readline
N, X = map(int, input().split())
S = input()[:-1]
INF = 10**18
half = INF//2
over_depth = 0
now = X
for s in S:
    if s == 'U':
        if over_depth:
            over_depth -= 1
        else:
            now //= 2
    else:
        if over_depth or now >= half:
            over_depth += 1
        else:
            now *= 2
            if s == 'R':
                now += 1

print(now)



