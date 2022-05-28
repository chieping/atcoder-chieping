H, W = map(int, input().split())
S = [input() for _ in range(H)]

points = []

for i, l in enumerate(S):
    if l.count('o') >= 1:
        for j, c in enumerate(l):
            if c == 'o':
                points.append((i, j))

print(points[1][0] - points[0][0] + abs(points[1][1] - points[0][1]))