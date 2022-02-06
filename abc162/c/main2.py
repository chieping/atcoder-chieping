# gcdを非再帰で実装すると全パターン計算しても間に合う
K = int(input())

def gcd(x, y):
    while y:
        r = x % y
        x = y
        y = r
    return x

ans = 0
for i in range(1, K+1):
    for j in range(1, K+1):
        for k in range(1, K+1):
            ans += gcd(gcd(i,j),k)
print(ans)
