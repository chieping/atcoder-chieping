from collections import deque


N, M = map(int, input().split())

ans = 0

# 訪問済み
mt = []
for i in range(N):
    mt.append([])

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    mt[a].append(b)

for n in range(N):
    #キュー
    Q = deque()
    # 訪問済み
    S = []
    for i in range(N):
        S.append(False)
    S[n] = True

    Q.append(n)
    ans += 1

    while len(Q) > 0:
        i = Q.popleft()

        for j in mt[i]:

            if not S[j]:
                Q.append(j)
                S[j] = True
                ans += 1

print(ans)

