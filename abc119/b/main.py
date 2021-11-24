N = int(input())
ans = 0
for i in range(N):
    x, u = input().split()
    if u == 'JPY':
        ans += int(x)
    elif u == 'BTC':
        ans += float(x) * 380000
print(ans)
