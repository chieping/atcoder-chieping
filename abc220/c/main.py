N = int(input())
A = list(map(int, input().split()))
X = int(input())
sum_loop = sum(A)

def f(n):
    d = n // N
    rem = n % N
    result = d * sum_loop
    for i in range(rem):
        result += A[i]
    return result

l = 0
r = 10 ** 20
mid = (l+r) // 2

while r - l > 1:
    if f(mid) > X:
        r = mid
    else:
        l = mid
    mid = (l+r) // 2

print(mid + 1)
