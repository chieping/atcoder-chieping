N, M = map(int, input().split())
sm, lg = sorted([N, M])

def naive(N, M):
    G = [[0] * (M) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if not(0 <= i+a < N): continue
                    if not(0 <= j+b < M): continue
                    G[i+a][j+b] += 1
    return sum(i % 2 for line in G for i in line)

def solve(sm, lg):
    if sm == 1:
        if lg == 1:
            return 1
        elif lg == 2:
            return 0
        else:
            return lg-2
    elif sm == 2:
        return 0
    else:
        return (sm-2) * (lg-2)

# nans = naive(sm, lg)
sans = solve(sm, lg)

# if nans != sans:
#     print(sm, lg)
#     print(nans)
#     print(sans)
# else:
#   print(sans)
print(sans)