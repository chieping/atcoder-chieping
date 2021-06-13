N, Q = map(int, input().split())

graph = []

for i in range(0, N):
    row = []
    for j in range(0, N):
        row.append(False)
    graph.append(row)

for _ in range(0, Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]
        y = query[2]
        x -= 1
        y -= 1
        graph[x][y] = True
        
    elif query[0] == 2:
        x = query[1]
        x -= 1
        for i in range(0, N):
            if graph[i][x]:
                graph[x][i] = True

    elif query[0] == 3:
        to_follow = []
        a = query[1]
        a -= 1
        for v in range(0, N):
            if graph[a][v]:
                for w in range(0, N):
                    if graph[v][w] and w != a:
                        to_follow.append(w)
        
        for w in to_follow:
            graph[a][w] = True
    
for i in range(0, N):
    l = map(lambda x: 'Y' if x else 'N', graph[i])
    print(''.join(l))

