N  = int(input())
A = [list(map(int, input().split())) for i in range(N)]

ALL = 1<<N

cost = [[10**100] * N for i in range(ALL)]

cost[0][0] = 0

def has_bit(n, i):
    return (n & (1<<i) > 0)

for n in range(ALL):
    for i in range(N):
        for j in range(N):
            if has_bit(n, j) or i == j:
                continue
            cost[n|(1<<j)][j] = min(cost[n|(1<<j)][j], cost[n][i] + A[i][j])

print(cost[ALL-1][0])
