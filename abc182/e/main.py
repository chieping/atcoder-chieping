from itertools import chain
import sys
readline = sys.stdin.readline
H, W, N, M = map(int, readline().split())
G = [[-1] + [0] * W + [-1] for _ in range(H+2)]
for _ in range(N):
    i, j = map(int, readline().split())
    G[i][j] = 2
for _ in range(M):
    i, j = map(int, readline().split())
    G[i][j] = -1
G[0] = [-1] * (W+2)
G[H+1] = [-1] * (W+2)

def light_horizontally(h, w):
    for i in range(1, h+1):
        j = 1
        light = False
        columnList = []
        while j <= w+1:
            if G[i][j] == -1:
                if light:
                    for k in columnList:
                        G[i][k] = 1
                columnList = []
                light = False
            light |= G[i][j] == 2
            if G[i][j] == 0:
                columnList.append(j)
            j += 1

light_horizontally(H, W)
G = list(map(list, zip(*G[::-1])))
light_horizontally(W, H)
print(sum(True for n in chain.from_iterable(G) if n >= 1))
