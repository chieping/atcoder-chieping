N = int(input())
A = list(map(int, input().split()))
A.sort()

def check(n):
    now = sum(A[:n+1])
    for b in A[n+1:]:
        if now*2 >= b:
            now += b
        else:
            return False
    return True

ok = N-1
ng = -1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(N-ok)