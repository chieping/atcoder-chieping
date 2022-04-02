N = int(input())

def f(a, b):
    return a**3 + a**2*b + a*b**2 + b**3
if N == 0:
    print(0)
    exit()

ans = 10**18+1
for i in range(10**6+1):
    ok = 10**6+1
    ng = 0
    if f(i, 0) >= N:
        ans = min(ans, f(i, 0))
    else:
        while ok-ng > 1:
            mid = (ok+ng)//2
            if f(i, mid) >= N:
                ok = mid
            else:
                ng = mid
        ans = min(ans, f(i, ok))

print(ans)
