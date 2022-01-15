N, K = map(int, input().split())
x = N
MOD = 10**5
vis = [-1] * (10**5+1)

def f(x):
    _sum = 0
    while x > 0:
        _sum += x % 10
        x //= 10
    return _sum

cnt = 0
while cnt < K:
    cnt += 1
    x = (x + f(x)) % MOD
    if vis[x] != -1:
        n = (K - cnt) // (cnt - vis[x])
        cnt += (cnt - vis[x]) * n
    else:
        vis[x] = cnt

print(x)
