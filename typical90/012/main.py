from union_find import UnionFind

H, W = map(int, input().split())
Q = int(input())
cells = [[False] * 2009 for _ in range(2009)]
uf = UnionFind(H*W)

def query1(r, c):
    for ar, ac in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
        if cells[ar][ac] == False:
            continue
        hash1 = (r-1)*W + (c-1)
        hash2 = (ar-1)*W + (ac-1)
        uf.union(hash1, hash2)
    cells[r][c] = True

def query2(ra, ca, rb, cb):
    if cells[ra][ca] == False or cells[rb][cb] == False:
        return False
    hash1 = (ra-1)*W + (ca-1)
    hash2 = (rb-1)*W + (cb-1)
    return uf.same(hash1, hash2)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        query1(*q[1:])

    elif q[0] == 2:
        ans = query2(*q[1:])
        if ans:
            print('Yes')
        else:
            print('No')
