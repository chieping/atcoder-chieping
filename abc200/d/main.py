from itertools import product
N = int(input())
A = list(map(int, input().split()))
# 鳩ノ巣原理により8個までで必ず答えが見つかる
ans = dict()
for bits in product([0, 1], repeat=min(N, 8)):
    seq = [i for bit, i in zip(bits, range(1, min(8, N)+1)) if bit == 1]
    if not len(seq): continue
    B = [A[i-1] for i in seq]
    m = sum(B) % 200
    if m in ans:
        ans1 = ans[m]
        print('Yes')
        print(len(ans1), *ans1)
        print(len(seq), *seq)
        exit()
    else:
        ans[m] = seq
print('No')
