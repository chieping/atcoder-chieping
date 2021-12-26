from bisect import bisect_left
N, Q = map(int, input().split())
A = list(map(int, input().split()))
# Ai以下の良い整数の個数を記録する
C = [0] * N
for i in range(N):
    C[i] = A[i] - i - 1

for _ in range(Q):
    k = int(input())
    if C[-1] < k:
        print(A[-1]+k-C[-1])
    else:
        idx = bisect_left(C, k)
        print(A[idx]-1-C[idx]+k)
