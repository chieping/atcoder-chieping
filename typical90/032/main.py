from itertools import permutations
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
U = [[False] * N for _ in range(N)]
INF = 10**18
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    U[x][y] = True
    U[y][x] = True

ans = INF
for P in permutations(range(N), N):
    succ = P[0]
    t = 0
    for i in range(N):
        if U[P[i]][succ]:
            t = INF
            break
        else:
            t += A[P[i]][i]
            succ = P[i]
        pass
    ans = min(ans, t)

if ans == INF:
    print(-1)
else:
    print(ans)
