from collections import defaultdict
INF = 10**18
N = int(input())
X, Y = map(int, input().split())
bentos = [list(map(int, input().split())) for i in range(N)]

# choice[i][(tako, tai)] = 選んだ個数
choice = [{} for i in range(N+1)]
choice[0][(0, 0)] = 0

for i in range(N):
    a, b = bentos[i]
    for tako in range(300):
        for tai in range(300):
            if (tako, tai) in choice[i]:
                k0 = choice[i][(tako, tai)]
            else:
                k0 = INF
            if (tako, tai) in choice[i+1]:
                k1 = choice[i+1][(tako, tai)]
            else:
                k1 = INF
            if (tako - a, tai - b) in choice[i]:
                k3 = choice[i][(tako - a, tai - b)]
            else:
                k3 = INF

            # 買わない場合
            # choice[i+1][(tako, tai)] = min(choice[i][(tako, tai)], choice[i+1][(tako, tai)])
            choice[i+1][(tako, tai)] = min(k0, k1, k3 + 1)
            # 買う場合
            # choice[i+1][(tako, tai)] = min(choice[i+1][(tako, tai)], choice[i][(tako - a, tai - b)] + 1)
            # choice[i+1][(tako, tai)] = min(k1, k3 + 1)

ans = INF
for (a, b) in choice[N]:
    if a >= X and b >= Y:
        ans = min(ans, choice[N][(a, b)])

if ans == INF:
    ans = -1

print(ans)



    
