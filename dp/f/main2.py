S = list(input())
T = list(input())
dp = [[0] * (len(T)+1) for i in range(len(S)+1)]

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])

ans = []
ans_len = dp[len(S)][len(T)]
i = len(S)
j = len(T)
while ans_len > 0:
    if dp[i][j] == ans_len and dp[i][j] > max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]):
        ans.append(S[i-1])
        ans_len -= 1
        i -= 1
        j -= 1
    else:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        if dp[i][j] == dp[i][j-1]:
            j -= 1

print(''.join(ans[::-1]))
