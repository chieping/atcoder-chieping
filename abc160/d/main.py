from collections import deque
N, X, Y = map(int, input().split())
X -= 1
Y -= 1
INF = 10**18
ans = [0] * N

for i in range(N):
    Q = deque()
    Q.append((i, 0))
    dist = [INF]*N
    dist[i] = 0
    while len(Q)>0:
        cur_v, cur_d = Q.pop()
        nxtd = cur_d+1
        if cur_v-1 >= 0 and nxtd < dist[cur_v-1] :
            dist[cur_v-1] = nxtd
            Q.append((cur_v-1, nxtd))
        if cur_v+1 < N and nxtd < dist[cur_v+1]:
            dist[cur_v+1] = nxtd
            Q.append((cur_v+1, nxtd))
        if X == cur_v and nxtd < dist[Y]:
            dist[Y] = nxtd
            Q.append((Y, nxtd))
        if Y == cur_v and nxtd < dist[X]:
            dist[X] = nxtd
            Q.append((X, nxtd))
    for d in dist:
        ans[d] += 1
ans = [a//2 for a in ans]
print(*ans[1:], sep='\n')
