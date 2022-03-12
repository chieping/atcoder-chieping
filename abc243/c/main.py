from collections import defaultdict
from pprint import pprint
import sys
input = sys.stdin.readline
N = int(input())

M = defaultdict(list)

for i in range(N):
    x, y = map(int, input().split())
    M[y].append((x, i))
S = input()[:-1]

for li in M.values():
    li.sort()

    p1 = False
    for x, i in li:
        if S[i] == 'R':
            p1 = True
        if S[i] == 'L' and p1:
            print('Yes')
            exit()

print('No')