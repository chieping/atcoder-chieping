from math import gcd
K = int(input())
ans = 0
for i in range(1, K+1):
    for j in range(1, K+1):
        g = gcd(i,j)
        for k in range(1, K+1):
            ans += gcd(g,k)
print(ans)
