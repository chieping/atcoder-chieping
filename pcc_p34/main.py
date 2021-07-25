N = int(input())
A = list(map(int, input().split()))
K = int(input())

def dfs(i, sum):
    if i == N: return sum == K
    if dfs(i + 1, sum): return True
    if dfs(i + 1, sum + A[i]): return True
    return False

if dfs(0, 0):
    print('Yes')
else:
    print('No')
