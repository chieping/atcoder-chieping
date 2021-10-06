from functools import reduce
from operator import add

H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

# 行ごとの合計と、列ごとの合計を持っておく
row = [sum(A[i]) for i in range(H)]
col = [reduce(add, [A[i][j] for i in range(H)]) for j in range(W)]

for i in range(H):
    print(*[row[i] + col[j] - A[i][j] for j in range(W)])
