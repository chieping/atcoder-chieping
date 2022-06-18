A = list(map(int, input().split()))
H = A[:3]
W = A[3:]

def meet(a, b, d, e):
    c = H[0] - a - b
    f = H[1] - d - e
    g = W[0] - a - d
    h = W[1] - b - e
    i1 = H[2] - g - h
    i2 = W[2] - c - f
    if i1 != i2:
        return False
    if any(1 > n for n in [c, f, g, h, i1]):
        return False
    return True

# 左上の4マスを決める
ans = 0
for a in range(1, 29):
    for b in range(1, 29):
        for d in range(1, 29):
            for e in range(1, 29):
                if meet(a, b, d, e):
                    ans += 1
print(ans)
