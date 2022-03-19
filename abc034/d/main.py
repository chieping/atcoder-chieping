N, K = map(int, input().split())
WP = [tuple(map(int, input().split())) for _ in range(N)]

def check(target):
    priority = []
    for w, p in WP:
        r = w * p / 100
        t = w * target / 100
        priority.append((r-t, w, p))
    priority.sort(reverse=True)
    W = 0
    S = 0
    for _, w, p in priority[:K]:
        W += w
        S += w * p / 100
    return S / W * 100 >= target


ok = 0
ng = 200
for _ in range(100):
    mid = (ok+ng)/2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)