from sys import stdin
n, q = map(int, stdin.readline().split())
# セグメント木 RAQ
SEG_LEN = 1<<18
seg = [0] * (SEG_LEN*2)

def add(l, r, x):
    l += SEG_LEN
    r += SEG_LEN
    while l < r:
        if l % 2 == 1:
            seg[l] += x
            l += 1
        l //= 2

        if r % 2 == 1:
            seg[r-1] += x
            r -= 1
        r //= 2

def get(idx):
    ans = 0
    idx += SEG_LEN
    ans += seg[idx]
    while True:
        idx //= 2
        if idx == 0:
            break
        ans += seg[idx]
    return ans
    
for _ in range(q):
    q, *params = list(map(int, stdin.readline().split()))
    if q == 0:
        (s, t, x) = params
        add(s, t+1, x)
    elif q == 1:
        i = params[0]
        print(get(i))
