from itertools import combinations
K = int(input())

def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)

ans = 0

# すべて同じ数の場合
ans += sum(range(1, K+1))
# うち2つが同じ数の場合
for i in range(1, K+1):
    for j in range(i+1, K+1):
        ans += 6*gcd(i,j)
# 3つの数が違う場合
for i,j,k in combinations(range(1, K+1), 3):
    ans += 6*gcd(gcd(i, j), k)

print(ans)
