H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
MOD = 998244353
ans = 1


# if K == 2:
#     pass

# m = H-1+W-1

# # 残り3回まで
# for i in range(K-3):
#     ans *= m
#     ans %= MOD
# # 残り3回目以降
# # 1. 行または列が同じところへ移動
# A = ((1 * (H-2)) + (1 * (W-2)))

# # 2. 行も列も違うところへ移動
# B = ((H-2)+(W-2)*2)

# print(A)
# print(B)
# ans *= (A+B)
# ans %= MOD




# A: HもWも不一致
Acnt = (H-1)*(W-1)
# B: H一致、W不一致
Bcnt = (W-1)
# C: H不一致、W一致
Ccnt = (H-1)
# D: Goal
Dcnt = 1

if K == 1:
    if x1 == x2 or y1 == y2:
        print(1)
    else:
        print(0)
    exit()
if K == 2:
    if x1 == x2 and y1 == y2:
        # Dパターン
        print(H-1+W-1)
    elif x1 == x2:
        # Bパターン
        print(W-2)
    elif y1 == y2:
        # Cパターン
        print(H-2)
    else:
        # Aパターン
        print(2)
    exit()
# K > 2

m = H-1+W-1
# 残り3回まで
for i in range(K-3):
    ans *= m
    ans %= MOD

# 残り3回以降

# Aパターン
ans *= 

print(ans)
