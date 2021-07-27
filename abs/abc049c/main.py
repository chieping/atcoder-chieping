from sys import setrecursionlimit

setrecursionlimit(100000)
S = input()

# dream dreamer erase eraser

# ↓これだとMLEになってしまう
# def dfs(s: str)-> bool:
#     if s == '':
#         return True
#     if s.startswith('dreamer'):
#         if dfs(s[7:]):
#             return True
#     if s.startswith('dream'):
#         return dfs(s[5:])
#     if s.startswith('eraser'):
#         if dfs(s[6:]):
#             return True
#     if s.startswith('erase'):
#         return dfs(s[5:])    
#     return False

def dfs(n: int)-> bool:
    if len(S) <= n:
        return True
    if S[n:n+7] == 'dreamer':
        if dfs(n+7):
            return True
    if S[n:n+5] == 'dream':
        return dfs(n+5)
    if S[n:n+6] == 'eraser':
        if dfs(n+6):
            return True
    if S[n:n+5] == 'erase':
        return dfs(n+5)    
    return False

ans = dfs(0)

if ans:
    print('YES')
else:
    print('NO')
