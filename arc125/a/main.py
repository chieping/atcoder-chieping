N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

if not set(T).issubset(set(S)):
    print(-1)
    exit()

# 切り替え回数
cnt = 0
pt = S[0]
for t in T:
    if pt != t:
        cnt += 1
    pt = t

if cnt == 0:
    first = 0
else:
    first = S.index(abs(S[0] - 1))
    first = min(first, S[::-1].index(abs(S[0] - 1)) + 1)
    cnt -= 1

print(M + cnt + first)