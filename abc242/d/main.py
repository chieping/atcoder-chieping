import sys
readline = sys.stdin.readline
S = readline()[:-1]
Q = int(readline())
TK = [tuple(map(int, readline().split())) for _ in range(Q)]

def popcount(param):
    n = param
    c = 0
    while n > 0:
        n, r = divmod(n, 2)
        c += r
    return c

for t, k in TK:
    k -= 1
    si = 0
    if t <= 60:
        b = 1<<t
        si = k//b
        k %= b
    r = popcount(k)
    l = t-r
    x = l + r*2 + (ord(S[si])-65)
    ans = chr(ord('A') + (x%3))
    print(ans)
