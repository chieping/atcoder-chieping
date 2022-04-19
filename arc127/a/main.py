N = int(input())
ans = 0
for i in range(1, 20):
    for j in range(20-i):
        m = int('1'*i + '0'*j)
        n = int('1'*(i-1) + '2' + '0'*j)
        r = min(N+1, n) - m
        ans += max(0, r)
print(ans)
