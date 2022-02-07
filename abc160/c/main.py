from itertools import accumulate


K, N = map(int, input().split())
A = list(map(int, input().split()))
A.append(K+A[0])
far = 0
for i in range(N):
    far = max(far, A[i+1] - A[i])
print(K-far)
