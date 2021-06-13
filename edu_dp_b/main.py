N, K = map(int, input().split())
h = list(map(int, input().split()))

costs = [0] * N

costs[0] = 0

for i in range(1, N):
    to = min(i, K)
    costs[i] = min(map(lambda k: costs[i - k] + abs(h[i - k] - h[i]), range(1, to + 1)))
        
print(costs[N - 1])
