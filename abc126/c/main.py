N, K = map(int, input().split())
n = K
# A: i回連続して表を出さないと負けになる閾値の数
A = []
while n > 1:
    A.append(n)
    n = (n+1)//2
A.append(n)

ans = 0.0
prev = N+1
for i, a in enumerate(A):
    if N >= a:
        ans += ((prev-a) / N)*(2**-i)
        prev -= prev-a
print(ans)
