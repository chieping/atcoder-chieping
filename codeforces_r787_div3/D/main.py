import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


for _  in int(input()):
    paths = []

    N = int(input())
    P = list(map(int, input().split()))
    root = -1
    edge = [[] for _ in range(N+1)]
    for i, p in enumerate(P, 1):
        if i == p:
            root = i
        else:
            edge[p].append(i)

    def dfs(u, path):
        global paths
        path.append(u)
        if len(edge[u]):
            dfs(edge[u][0], path)
            if len(edge[u]) > 1:
                for v in edge[u][1:]:
                    dfs(v, [])
        else:
            paths.append(path)

    dfs(root, [])
    print(len(paths))
    for ans in paths:
        print(len(ans))
        print(*ans)
    print()
