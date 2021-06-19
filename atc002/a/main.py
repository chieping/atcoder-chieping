import collections

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

M = [input() for i in range(R)]

S = [[-1] * C for _ in range(R)]
S[sy-1][sx-1] = 0

visited = [[False] * C for i in range(R)]
visited[sy-1][sx-1] = True

Q = collections.deque()

Q.append((sy-1, sx-1))

while len(Q) > 0:
    y, x = Q.popleft()
    s = S[y][x]

    if M[y+1][x] != '#' and not visited[y+1][x]:
        Q.append((y+1, x))
        S[y+1][x] = s + 1
        visited[y+1][x] = True
    if M[y][x+1] != '#' and not visited[y][x+1]:
        Q.append((y, x+1))
        S[y][x+1] = s + 1
        visited[y][x+1] = True
    if M[y-1][x] != '#' and not visited[y-1][x]:
        Q.append((y-1, x))
        S[y-1][x] = s + 1
        visited[y-1][x] = True
    if M[y][x-1] != '#' and not visited[y][x-1]:
        Q.append((y, x-1))
        S[y][x-1] = s + 1
        visited[y][x-1] = True

print(S[gy-1][gx-1])
