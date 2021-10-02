from collections import defaultdict


N = int(input())
A = defaultdict(int)
B = defaultdict(int)
for i in range(N):
    a, b = map(int, input().split())
    A[a-1] += 1
    A[a-1+b] -= 1




tmp = 0
ans = [0] * (N+1)
for i, j in sorted(A.items()):
    tmp += j
    
    ans[j] += i
    print(i, j)

print(*ans[1:])
