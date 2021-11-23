import sys
sys.setrecursionlimit(10**6)

H, W, A, B = map(int, input().split())
used = [[False] * 20 for _ in range(20)]

# 長い畳の置き方が決まれば1x1の畳の置き方は自動的に一つに決まるので、
# 長い畳の置き方が決まればよい。
# 左上から順に、長い畳を横に置くか縦に置く、または置かないの3つの
# 置き方を順に試す
# 右下まで試したときに長い畳が0枚になっていれば+1する
# DFSで全パターンを試す

def dfs(i, j, a):
    if i == H and j == W:
        return 1 if a == 0 else 0
    if j > W:
        return dfs(i+1, 1, a)
    
    ret = 0
    # 横置き
    if a > 0 and used[i][j] == False and used[i][j+1] == False and j+1 <= W:
        used[i][j] = True
        used[i][j+1] = True
        ret += dfs(i, j+1, a-1)
        used[i][j] = False
        used[i][j+1] = False
    
    # 縦置き
    if a > 0 and used[i][j] == False and used[i+1][j] == False and i+1 <= H:
        used[i][j] = True
        used[i+1][j] = True
        ret += dfs(i, j+1, a-1)
        used[i][j] = False
        used[i+1][j] = False
    
    # 置かない
    ret += dfs(i, j+1, a)
    return ret
    
ans = dfs(1, 1, A)
print(ans)
