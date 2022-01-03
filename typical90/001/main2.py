from sys import stdin
N, L = map(int, stdin.readline().split())
K = int(stdin.readline())
A = list(map(int, stdin.readline().split())) + [L]

def is_ok(n):
    i = 0
    k = K
    left = 0
    while i <= N:
        if A[i]-left >= n:
            k -= 1
            if k < 0:
                return True
            left = A[i]
        else:
            i += 1
    return False

ok = 0
ng = L
while ng-ok > 1:
    mid = (ok+ng)//2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
