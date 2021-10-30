import sys
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())

edges = [[] for i in range(N)]
# 入次数
indeg = [0] * N

for i in range(M):
    x, y = map(int, input().split())
    edges[x-1].append(y-1)
    indeg[y-1] += 1

# length[i]: 頂点iから始まるパスの最大長
length = [0] * N
# done[i]: length[i]がすでに計算済みであることを示すフラグ
done = [False] * N

def rec(i):
    if done[i]:
        return length[i]
    length[i] = 0
    for j in edges[i]:
        length[i] = max(length[i], rec(j) + 1)
    done[i] = True
    return length[i]

for i in range(N):
    if indeg[i] == 0:
        rec(i)

print(max(length))
