from sys import stdin
n, q = map(int, stdin.readline().split())
INF = (1<<31)-1
# セグメント木 RMQ
seg = [INF] * (1<<20)

def set_value(pos, val):
    pos += 1<<19
    seg[pos] = val
    pos //= 2
    while pos > 0:
        seg[pos] = min(seg[pos*2], seg[pos*2+1])
        pos //= 2

def get_min(ql, qr, sl = 0, sr = 1<<19, pos = 1):
    # 全く被っていない場合
    if qr <= sl or sr <= ql:
        return INF
    
    # 完全に包まれている場合
    if ql <= sl and sr <= qr:
        return seg[pos]

    # 部分的に被っている場合は再帰
    sm = (sl + sr) // 2
    lmin = get_min(ql, qr, sl, sm, pos*2)
    rmin = get_min(ql, qr, sm, sr, pos*2 + 1)
    return min(lmin, rmin)

for _ in range(q):
    com, x, y = list(map(int, stdin.readline().split()))

    if com == 0:
        set_value(x, y)
    elif com == 1:
        print(get_min(x, y+1))
