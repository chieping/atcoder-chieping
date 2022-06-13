N, D, K = map(int, input().split())
L = [0] * D
R = [0] * D
for i in range(D):
    L[i], R[i] = map(lambda x: int(x) - 1, input().split())
S = [0] * K
T = [0] * K
for i in range(K):
    S[i], T[i] = map(lambda x: int(x) - 1, input().split())

ans = [-1] * K
now = S.copy()

for i, l, r in zip(range(1, D+1), L, R):
    for j in range(K):
        # 到達済み？
        if ans[j] != -1: continue
        # 到達した
        if l <= now[j] <= r and l <= T[j] <= r:
            ans[j] = i
        # 動くことが可能？
        if l <= now[j] <= r:
            # 貪欲に移動
            if now[j] < T[j]:
                now[j] = r
            else:
                now[j] = l
print(*ans, sep='\n')
