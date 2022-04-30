import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
edge = [[] for _ in range(N)]
ans = [0] * (N-1)
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    edge[a].append((b, i))
    edge[b].append((a, i))

def dfs(n, last=-1):
    color = 1
    for v, i in edge[n]:
        if ans[i] == 0:
            if color == last:
                color += 1
            ans[i] = color
            dfs(v, color)
            color += 1

dfs(0)
print(max(ans))
print(*ans, sep='\n')
