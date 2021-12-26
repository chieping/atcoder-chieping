from itertools import combinations
N = int(input())
V = [tuple(map(int, input().split() + [i])) for i in range(N)]
V2 = []

for i in range(2):
    V.sort(key=lambda x: x[i])
    V2.append(V[0])
    V2.append(V[1])
    V2.append(V[-1])
    V2.append(V[-2])

D = []
for a, b in combinations(set(V2), 2):
    D.append(max(abs(a[0]-b[0]), abs(a[1]-b[1])))
print(sorted(D)[-2])
