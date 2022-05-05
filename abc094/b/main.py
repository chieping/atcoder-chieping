from bisect import bisect_left
N, M, X = map(int, input().split())
A = list(map(int, input().split()))
i = bisect_left(A, X)
print(min(i, M-i))
