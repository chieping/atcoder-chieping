from collections import deque

N, X, Y = map(int, input().split())

X += 201
Y += 201

obstruction = []

for i in range(0, 403):
    row = []
    for j in range(0, 403):
        row.append(False)
    obstruction.append(row)

for _ in range(0, N):
    ox, oy = map(int, input().split())
    obstruction[oy + 201][ox + 201] = True

dist = []
for i in range(0, 403):
    dist.append([-1] * 403)
dist[201][201] = 0

Q = deque()

Q.append([201, 201])

while len(Q) > 0:
    y, x = Q.popleft()

    for y2, x2 in [[y+1, x-1],[y+1, x],[y+1,x+1],[y, x-1], [y,x+1],[y-1, x]]:

        if not (0 <= y2 <= 402 and 0 <= x2 <= 402):
            continue

        if obstruction[y2][x2]:
            continue

        if dist[y2][x2] == -1:
            dist[y2][x2] = dist[y][x] + 1
            Q.append([y2, x2])

print(dist[Y][X])
