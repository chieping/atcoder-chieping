from pprint import pprint
import sys
readline = sys.stdin.readline
S = readline()[:-1]
A = [ord(s) - 65 for s in list(S)] # A:0, B:1, C:2 に変換
Slen = len(S)
Q = int(readline())
TK = [tuple(map(int, readline().split())) for _ in range(Q)]
TK.sort()

def to_c(i):
    if i == 0:
        return 'A'
    elif i == 1:
        return 'B'
    else:
        return 'C'

curr = 0
now = 2
for t, k in TK:
    k -= 1
    while t > 0:
        d, r = divmod(k, 2)
        t -= 1
    

