import sys
sys.setrecursionlimit(1000000)

N = int(input())

child = [[] for i in range(N)]

for i in range(1, N):
    b = int(input())
    child[b-1].append(i)

def dfs(i):
    if len(child[i]) == 0:
        return 1
    else:
        values = [dfs(j) for j in child[i]]
        return max(values) + min(values) + 1

print(dfs(0))
