from itertools import combinations
N = int(input())
V = [list(map(int, input().split())) for i in range(N)]
V2 = []

V.sort(key=lambda x: x[0])
if len(V): V2.append(V.pop(0))
if len(V): V2.append(V.pop(0))
if len(V): V2.append(V.pop(-1))
if len(V): V2.append(V.pop(-1))

V.sort(key=lambda x: x[1])
if len(V): V2.append(V.pop(0))
if len(V): V2.append(V.pop(0))
if len(V): V2.append(V.pop(-1))
if len(V): V2.append(V.pop(-1))

D = []
for a, b in combinations(V2, 2):
    D.append(max(abs(a[0]-b[0]), abs(a[1]-b[1])))
D.sort()
print(D[-2])
