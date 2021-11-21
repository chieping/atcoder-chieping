N, K = map(int, input().split())
P = [sum(map(int, input().split())) for _ in range(N)]
T = sorted(P)[-K]
for i in range(N):
    if P[i] + 300 >= T:
        print('Yes')
    else:
        print('No')
