N, L, R = map(int, input().split())
ans = 0
for i in range(100):
    if ((1<<i) ^ N) < N:
        a = min((1<<i+1)-1, R)
        b = max((1<<i), L)
        ans += max(0, a-b+1)
print(ans)
