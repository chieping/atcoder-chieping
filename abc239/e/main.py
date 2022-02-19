# WA
import heapq
from pprint import pprint
import sys
readline = sys.stdin.readline

N, Q = map(int, readline().split())
X = list(map(int, readline().split()))

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    def nums(self):
        res = [self.data]
        if self.left:
            res = list(heapq.merge(res, self.left.nums()))
        if self.right:
            res = list(heapq.merge(res, self.right.nums()))
        return res

nodes = [Node(x) for x in X]
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
        if not nodes[n].left:
            nodes[n].left = nodes[v]
        else:
            nodes[n].right = nodes[v]
        dfs(v, n)

dfs(0, 0)

for _ in range(Q):
    v, k = map(int, readline().split())
    v -= 1
    k -= 1
    nums = nodes[v].nums()
    print(nums[len(nums)-1-k])
