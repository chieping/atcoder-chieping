import sys
sys.setrecursionlimit(10**6)

H, W, A, B = map(int, input().split())

def dfs(x, y, a):
    if H == y:
        return a == 0
    if W == x:
        return dfs(0, y + 1, a)
    if used[y][x]:
        return dfs(x + 1, y, a)
    
    res = 0

    # 縦置き
    if y + 1 < H and not used[y+1][x] and 0 < a:
        used[y][x] = True
        used[y+1][x] = True
        res += dfs(x + 1, y, a - 1)
        used[y][x] = False
        used[y+1][x] = False
    
    # 横置き
    if x + 1 < W and not used[y][x + 1] and 0 < a:
        used[y][x] = True
        used[y][x+1] = True
        res += dfs(x + 1, y, a - 1)
        used[y][x] = False
        used[y][x+1] = False
    
    # 何も置かない
    res += dfs(x + 1, y, a)

    return res

used = [[False] * W for i in range(H)]

ans = dfs(0, 0, A)

print(ans)
