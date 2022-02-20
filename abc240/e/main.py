import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(readline())

class Node:
    def __init__(self, key):
        self.data = key
        self.L = -1
        self.R = -1
        self.children = []

    def leaves(self):
        if not self.children:
            return 1
        return sum(c.leaves() for c in self.children)

nodes = [Node(i) for i in range(N)]
edges = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

def dfs(n, ex):
    for v in edges[n]:
        if v == ex:
            continue
        nodes[n].children.append(nodes[v])
        dfs(v, n)

dfs(0, 0)

ans = [[0, 0] for i in range(N)]

root = nodes[0]
root.L = 1
root.R = root.leaves()

ans[0] = [root.L, root.R]

def dfs2(i):
    node = nodes[i]
    i = 1
    for c in node.children:
        c.L = i
        c.R = i + c.leaves() - 1
        i = c.R+1
        dfs2(c.data)

dfs2(0)

for i in range(N):
    node = nodes[i]
    ans[i] = [node.L, node.R]

for a in ans:
    print(*a)
