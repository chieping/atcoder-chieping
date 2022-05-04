N, M = map(int, input().split())
ans = 0
i = 1
while i*i <= M:
    d, r = divmod(M, i)
    if r == 0:
        if d >= N:
            ans = max(ans, i)
        if i >= N:
            ans = max(ans, d)
    i += 1
print(ans)
