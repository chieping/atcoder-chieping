from itertools import permutations
from pprint import pprint


N, M = map(int, input().split())

# A = []
# B = []
# C = []
# D = []
# for i in range(M):
#     a, b = map(int, input().split())
#     A.append(a)
#     B.append(b)
# for i in range(M):
#     c, d = map(int, input().split())
#     C.append(c)
#     D.append(d)
edgesA = []
edgesC = []
for i in range(M):
    a, b = map(int, input().split())
    edgesA.append([a, b])
    edgesA.append([b, a])
edgesA.sort()
for i in range(M):
    c, d = map(int, input().split())
    edgesC.append([c, d])
    edgesC.append([d, c])


for p in permutations(range(1, N+1)):
    # pprint(p)
    p = [0] + list(p)
    # CN = list(map(lambda x: p[x], C))
    # pprint(C)
    # pprint(CN)
    # DN = list(map(lambda x: p[x], D))
    edgedCC = list(map(lambda x: [p[x[0]], p[x[1]]], edgesC))
    edgedCC.sort()

    if edgesA == edgedCC:
        print('Yes')
        exit()
print('No')
