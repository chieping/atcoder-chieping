N, K = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) <= K:
    ans = 0
    for a in A:
        # 等差数列の和
        ans += a * (a+1) // 2
    print(ans)
    exit()

def ok(line):
    cnt = 0
    for a in A:
        if (a >= line):
            cnt += a - line
    return cnt <= K

bottom = 0
top = max(A)

while top - bottom > 1:
    mid = (top + bottom) // 2
    if ok(mid):
        top = mid
    else:
        bottom = mid

line = top
ans = 0
for a in A:
    if a >= line:
        K -= a - line
        ans += (line + 1 + a) * (a - line) // 2

ans += K * line
print(ans)
