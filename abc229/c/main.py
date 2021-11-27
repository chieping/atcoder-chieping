N, W = map(int, input().split())
C = [list(map(int, input().split())) for i in range(N)]

C.sort(reverse=True)

w = 0
ans = 0
i = 0


for oo, ww in C:
    if W <= w:
        break
    cw = min(ww, W-w)
    w = w + cw
    ans += oo * cw
print(ans)
