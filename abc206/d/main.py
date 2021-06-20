from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

N = int(input())
A = list(map(int, input().split()))

edges = defaultdict(set)

for i in range(N//2):
    if A[i] == A[N-1-i]:
        continue

    edges[A[i]].add(A[N-1-i])
    edges[A[N-1-i]].add(A[i])

visited = [False] * (2*(10**5)+1)

def dfs(a, visited):
    stack = [a]
    cnt = 0
    while stack:
        a = stack.pop()
        if visited[a]:
            continue
        cnt += 1
        visited[a] = True
        for b in edges[a]:
            stack.append(b)
    return cnt

ans = 0
for a in set(A):
    if visited[a]:
        continue
    cnt = dfs(a, visited)
    ans += (cnt - 1)

print(ans)    
