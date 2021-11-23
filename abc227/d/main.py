N, K = map(int, input().split())
A = list(map(int, input().split()))
ng = 10**18
ok = 0
while ng-ok > 1:
    mid = (ok+ng)//2
    s = sum([min(x, mid) for x in A])
    if s >= K*mid:
        ok = mid
    else:
        ng = mid
print(ok)
