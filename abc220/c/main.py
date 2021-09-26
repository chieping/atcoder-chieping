N = int(input())
A = list(map(int, input().split()))
X = int(input())
sum_loop = sum(A)

def check(n):
    d = n // N
    rem = n % N
    result = d * sum_loop
    for i in range(rem):
        result += A[i]
    return result

ng = 0
ok = 10 ** 20
mid = (ng+ok) // 2

while ok - ng > 1:
    if check(mid) > X:
        ok = mid
    else:
        ng = mid
    mid = (ng+ok) // 2

print(ok)
