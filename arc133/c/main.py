# 未提出
from pprint import pprint
import sys
readline = sys.stdin.readline
H, W, K = list(map(int, readline().split()))
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))

if sum(A) % K != sum(B) % K:
    print(-1)
    exit()

# G = [[0] * W for _ in range(H)]

# # 横の数値を決める
# for i in range(H-1):
#     a = A[i]
#     for j in range(W-1):
#         G[i][j] = K-1
#     G[i][-1] = a-((W-1)*(K-1)%K)

# # 最終行の数字を決める
# for j in range(W):
#     b = B[j]
#     tmp = 0
#     for i in range(H):
#         tmp += G[i][j]
#     G[-1][j] = b-(tmp%K)

# pprint(G)
# ans = 0
# for i in range(H):
#     ans += sum(G[i])
# print(ans)

