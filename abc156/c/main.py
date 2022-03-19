N = int(input())
X = [0] + list(map(int, input().split()))
ans = 10**18
for p in range(1, 101):
    res = 0
    for i in range(1, N+1):
        res += (X[i] - p)**2
    ans = min(ans, res)
print(ans)
