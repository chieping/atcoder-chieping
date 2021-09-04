N = int(input())
P = list(map(int, input().split()))

Q = [-1] * (N+1)

for i in range(N):
    p = P[i]
    Q[p] = i+1

print(*Q[1:])
