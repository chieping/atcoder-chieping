from itertools import permutations
N, M = map(int, input().split())
edgesA = []
for i in range(M):
    a, b = map(int, input().split())
    edgesA.append([a, b])
    edgesA.append([b, a])
edgesC = []
for i in range(M):
    c, d = map(int, input().split())
    edgesC.append([c, d])
    edgesC.append([d, c])

edgesA.sort()
ans = False
for p in permutations(range(1, N+1)):
    edgesCC = [[p[c-1], p[d-1]] for (c, d) in edgesC]
    edgesCC.sort()
    ans |= (edgesA == edgesCC)
print('Yes' if ans else 'No')
