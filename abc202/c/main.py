from collections import defaultdict

N = int(input())
A = list(map(lambda x: x-1, map(int, input().split())))
B = list(map(lambda x: x-1, map(int, input().split())))
C = list(map(lambda x: x-1, map(int, input().split())))

count = defaultdict(int)

for j in range(N):
    count[B[C[j]]] += 1

ans = 0
for i in range(N):
    ans += count[A[i]]

print(ans)
