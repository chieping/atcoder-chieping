import sys
input = sys.stdin.readline
N, X = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 10**30
MinB = 10**30
SumA = 0
SumB = 0
for i in range(N):
    if X <= i: break
    SumA += A[i]
    SumB += B[i]
    MinB = min(MinB, B[i])
    ans = min(ans, SumA + SumB + MinB*(X-i-1))
    # print(SumA, SumB, MinB, SumA + SumB + MinB*(X-i-1))

print(ans)