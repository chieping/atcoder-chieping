N = int(input())
A = []
for i in range(N):
    a, b = map(int, input().split())
    A.append((a, 1))
    A.append((a+b, -1))

A.sort()

tmp = 0
ans = [0] * (N+1)

for i in range(len(A)-1):
    tmp += A[i][1]
    ans[tmp] += (A[i+1][0] - A[i][0])

print(*ans[1:])
