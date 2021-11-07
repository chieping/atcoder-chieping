N, M = map(int, input().split())
edges = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

ans = 0
for i in range(N):
    # if len(list(filter(lambda x: x < i, edges[i]))) == 1:
    if len([x for x in edges[i] if x < i]) == 1:
        ans += 1
print(ans)
