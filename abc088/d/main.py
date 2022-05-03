from collections import deque
H, W = map(int, input().split())
S = ['#' + input() + '#' for _ in range(H)]
S.insert(0, '#' * (W+2))
S.append('#' * (W+2))
INF = 10**9
white = sum(s.count('.') for s in S)
dist = [[INF] * (W+2) for _ in range(H+2)]
dist[1][1] = 0
q = deque()
q.append((1, 1))
while len(q):
    i, j = q.popleft()
    if i == H and j == W:
        print(white - dist[i][j] - 1)
        exit()
    for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        if S[i+di][j+dj] == '#': continue
        if dist[i+di][j+dj] != INF: continue
        dist[i+di][j+dj] = dist[i][j] + 1
        q.append((i+di, j+dj))
print(-1)