N = int(input())
T = [0] * (N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    T[a] += 1
    T[b] += 1

if max(T) == N-1:
    print('Yes')
else:
    print('No')
