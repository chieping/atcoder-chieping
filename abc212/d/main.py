from heapq import heappop, heappush

Q = int(input())

bag = [10**18]

# 出力されるときに追加されるべき数
added = 0

for i in range(Q):
    q = input()
    if q == '3':
        n = heappop(bag)
        print(n + added)
    elif q[0] == '1':
        _, x = map(int, q.split())
        heappush(bag, x - added)
    else:
        # 2
        _, x = map(int, q.split())
        # bag = [ n + x for n in bag]
        added += x
