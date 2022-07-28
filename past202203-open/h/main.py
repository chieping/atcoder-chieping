N, Q = map(int, input().split())
parent = list(range(N+1))
vert = [[i] for i in range(N+1)]

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        u, v = q[1:]
        if parent[u] != parent[v]:
            if len(vert[parent[u]]) < len(vert[parent[v]]):
                u, v = v, u
            a, b = parent[u], parent[v]
            for x in vert[b]:
                vert[a].append(x)
                parent[x] = a
            vert[b] = []
    else:
        u = q[1]
        vert[parent[u]].sort()
        print(*vert[parent[u]])
