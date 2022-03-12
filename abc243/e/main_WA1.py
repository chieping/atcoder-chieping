# WA
# 最小全域木で解けるかと思ったが、
# 最小全域木は、全ての頂点を結ぶ木の、辺の重みを
# 最小化するもので、各頂点間の距離が変わることがある
# ため、解法としておかしかった。
import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

edge = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((c, b, i))
    edge[b].append((c, a, i))

used = set()

def f(start):
    marked = [False] * N
    marked_count = 0
    marked[start] = True
    marked_count += 1
    Q = []
    for c, i, e in edge[start]:
        heapq.heappush(Q, (c, i, e))

    while marked_count < N:
        c, i, e = heapq.heappop(Q)

        if marked[i]:
            continue

        marked[i] = True
        marked_count += 1
        used.add(e)

        for (c, j, e) in edge[i]:
            if marked[j]:
                continue
            heapq.heappush(Q, (c, j, e))

f(0)
print(M-len(used))
