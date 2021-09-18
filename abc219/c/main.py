import heapq


X = input()
N = int(input())
S = [input() for i in range(N)]

M = {}
for i in range(len(X)):
    M[X[i]] = i

heap = []

for name in S:
    order = []
    for s in name:
        order.append(M[s])
    
    heapq.heappush(heap, (order, name))

while len(heap) > 0:
    print(heapq.heappop(heap)[1])
