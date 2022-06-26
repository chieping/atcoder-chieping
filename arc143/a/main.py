A = list(map(int, input().split()))
A.sort()
if A[0] + A[1] < A[2]:
    print(-1)
    exit()
ans = A[2]
print(A[2])