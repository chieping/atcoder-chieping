N, a, b = map(int, input().split())
A = list(map(int, input().split()))
ok = min(A)
ng = sum(A) // N + 1

def check(n):
    sumA = 0
    sumB = 0
    for i in A:
        if i > n:
            sumB += (i-n)//b
        if i < n:
            sumA += (n-i+a-1)//a
    return sumA <= sumB


while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
