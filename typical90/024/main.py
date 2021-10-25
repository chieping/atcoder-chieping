from functools import reduce
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
diff = reduce(lambda x, y: x+y, [abs(A[i] - B[i]) for i in range(N)])
if K < diff or (K-diff) % 2 == 1:
    print('No')
else:
    print('Yes')
