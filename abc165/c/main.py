from itertools import combinations_with_replacement
N, M, Q = map(int, input().split())

A = []
B = []
C = []
D = []
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    a -= 1; b -= 1
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

P = list(zip(A, B, C, D))

# 全探索する。
# この場合の広義単調増加数列の全列挙は、nCr(N+M-1, N) で作ることができる。

ans = 0
# 0を数値、1を仕切りとして順列で作ったが遅すぎた
# for cand in permutations([0] * (M-1) + [1] * N):
#     zero_cnt = 0
#     score = 0
#     A = []
#     for c in cand:
#         if c == 0:
#             zero_cnt += 1
#         else:
#             A.append(zero_cnt + 1)
#     for a, b, c, d in P:
#         if A[b] - A[a] == c:
#             score += d
#     ans = max(ans, score)

# combinations_with_replacementでできた
for cand in combinations_with_replacement(range(1, M+1), N):
    score = 0
    for a, b, c, d in P:
        if cand[b] - cand[a] == c:
            score += d
    ans = max(ans, score)
print(ans)