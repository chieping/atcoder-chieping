N = int(input())
ans = 10**15
i = 1
while i*i <= N:
    div, r = divmod(N, i)
    if r == 0:
        ans = min(ans, div+i-2)
    i += 1
print(ans)
