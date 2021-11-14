from collections import deque
H, W = map(int, input().split())
Q = int(input())
cells = [[False]*W for i in range(H)]
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        r, c = (x-1 for x in q[1:])
        cells[r][c] = True
    elif q[0] == 2:
        ra, ca, rb, cb = (x-1 for x in q[1:])
        if not (cells[ra][ca] and cells[rb][cb]):
            print('No')
        else:
            q = deque()
            visited = [[False]*W for i in range(H)]
            visited[ra][ca] = True
            q.append((ra, ca))
            while len(q) > 0:
                r, c = q.pop()
                for rnext, cnext in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
                    if (not 0 <= rnext < H) or (not 0 <= cnext < W):
                        continue
                    if cells[rnext][cnext] and not visited[rnext][cnext]:
                        visited[rnext][cnext] = True
                        q.append((rnext, cnext))
            if visited[rb][cb]:
                print('Yes')
            else:
                print('No')
