from itertools import permutations
import sys
N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M = int(sys.stdin.readline())
INF = 10**18
kenaku = [[False] * N for _ in range(N)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    x, y = x-1, y-1
    kenaku[x][y] = True
    kenaku[y][x] = True

def ok(runners):
    prev = runners[0]
    for next in runners[1:]:
        if kenaku[prev][next]:
            return False
        else:
            prev = next
    return True

ans = INF
for runners in permutations(range(N)):
    if not ok(runners):
        continue
    ans = min(ans, sum(A[runners[i]][i] for i in range(N)))

print(-1 if ans == INF else ans)
