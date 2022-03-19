from math import gcd
L, R = map(int, input().split())
ans_r = 10**18
for i in range(1000):
    for j in range(1000):
        if gcd(L+i, R-j) == 1:
            ans_r = min(ans_r, i+j)
print(R-L-ans_r)
