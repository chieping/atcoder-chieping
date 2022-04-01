import sys
input = sys.stdin.readline
N, S = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
dp = [[False] * (S+1) for _ in range(N+1)]
dp[0][0] = True
for i, [a, b] in enumerate(AB, 1):
    for j in range(S+1):
        if j-a >= 0 and dp[i-1][j-a]:
            dp[i][j] = True
        if j-b >= 0 and dp[i-1][j-b]:
            dp[i][j] = True

if not dp[N][S]:
    print('Impossible')
    exit()

cur = S
ans = []
for i, [a, b] in zip(range(N-1, -1, -1), AB[::-1]):
    if cur-a >= 0 and dp[i][cur-a]:
        ans.append('A')
        cur -= a
    else:
        ans.append('B')
        cur -= b

print(''.join(ans[::-1]))