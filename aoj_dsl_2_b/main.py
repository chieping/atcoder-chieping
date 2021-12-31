from sys import stdin
n, q = map(int, stdin.readline().split())
# セグメント木 RSQ
SEG_LEN = 1<<18
seg = [0] * (SEG_LEN*2)

def add(idx, v):
    idx += SEG_LEN
    seg[idx] += v
    while True:
        idx //= 2
        if idx == 0:
            break
        seg[idx] = seg[idx*2] + seg[idx*2+1]

def getSum(l, r):
    l += SEG_LEN
    r += SEG_LEN
    ans = 0
    while l < r:
        if l % 2 == 1:
            ans += seg[l]
            l += 1
        l //= 2

        if r % 2 == 1:
            ans += seg[r-1]
            r -= 1
        r //= 2
    return ans

for _ in range(q):
    com, x, y = map(int, stdin.readline().split())

    if com == 0: # add
        add(x, y)
    elif com == 1: # getSum
        print(getSum(x, y+1))
