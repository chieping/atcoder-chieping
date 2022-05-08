H, W = map(int, input().split())
R, C = map(int, input().split())
ans = 0
if H > 1:
    ans += 1
    if 1 < R < H:
        ans += 1
if W > 1:
    ans += 1
    if 1 < C < W:
        ans += 1
print(ans)
