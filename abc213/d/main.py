import sys
sys.setrecursionlimit(300000)

N = int(input())

G = [[] for i in range(N+1)]

for i in range(N-1):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

for i in range(N+1):
    G[i].sort()

ans = []

def dfs(crr, pre):
    ans.append(crr)

    for next in G[crr]:
        if next != pre:
            dfs(next, crr)
            ans.append(crr)

dfs(1, -1)

print(*ans)
