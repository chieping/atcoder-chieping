N, K = map(int, input().split())
P = [(sum(map(int, input().split())), i) for i in range(N)]
P.sort()

kijun = P[-K][0]

ans = []
for i in range(N):
    if (P[i][0] + 300) >= kijun:
        a = 'Yes'
    else:
        a = 'No'
    ans.append((P[i][1], a))

ans.sort()

for i in range(N):
    print(ans[i][1])
