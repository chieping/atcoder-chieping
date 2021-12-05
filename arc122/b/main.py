import itertools


N = int(input())
A = list(map(int, input().split()))
A.sort()
acc = list(itertools.accumulate(A))
ans = 10**18
for i in range(N):
    x = A[i] / 2
    ans = min(ans, (x*N) + acc[N-1]-acc[i] - (x*2*(N-i-1)))
print(ans/N)
