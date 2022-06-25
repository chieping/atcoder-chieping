from collections import defaultdict
N = int(input())
S = list(map(int, list(input())))
W = list(map(int, input().split()))
X = defaultdict(list)
for i, w in enumerate(W):
    X[w].append(i)
# 0のときは全員大人と判定される
now = S.count(1)
ans = now
for w in sorted(X.keys()):
    for i in X[w]:
        if S[i] == 0:
            now += 1
        else:
            now -= 1
    ans = max(ans, now)
print(ans)
