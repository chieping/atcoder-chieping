S = list(input())
T = list(input())
sl = len(S)
tl = len(T)
dp = [[0] * (tl+1) for _ in range(sl+1)]

for i in range(1, sl+1):
    for j in range(1, tl+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ansl = dp[sl][tl]
S = [''] + S
T = [''] + T
i = sl
j = tl
ans_r = []
while ansl > 0:
    if S[i] == T[j]:
        ans_r.append(S[i])
        i -= 1
        j -= 1
        ansl -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        j -= 1
print(''.join(ans_r[::-1]))
