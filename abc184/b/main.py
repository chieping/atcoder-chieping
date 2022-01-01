from sys import stdin
N, X = map(int, stdin.readline().split())
S = stdin.readline()[:-1]
ans = X
for s in S:
    if s == 'o':
        ans += 1
    else:
        ans = max(ans-1, 0)
print(ans)
