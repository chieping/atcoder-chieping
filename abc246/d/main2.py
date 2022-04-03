# 公式解説 二分探索を使わない
N = int(input())
def f(a, b):
    return a**3 + a**2*b + a*b**2 + b**3
ans = 10**18
i = 0
j = 10**6
while i <= j:
    cf = f(i, j)
    if cf >= N:
        ans = min(ans, cf)
        j -= 1
    else:
        i += 1
print(ans)