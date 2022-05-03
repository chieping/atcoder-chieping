# 解説AC
# ポイントはa1を0と仮定して考えてもよいということ
C = [list(map(int, input().split())) for _ in range(3)]
A = [0, 0, 0]
B = [C[0][0], C[0][1], C[0][2]]
A[1] = C[1][1] - B[1]
A[2] = C[2][2] - B[2]
ans = all(C[i][j]==A[i]+B[j] for i in range(3) for j in range(3))
print('Yes' if ans else 'No')