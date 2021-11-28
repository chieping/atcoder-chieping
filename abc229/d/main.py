# .を1, Xを0に変換する
A = [1 if s == "." else 0 for s in input()]
K = int(input())
n = len(A)
ans = 0
# 尺取り法
r = 0
s = 0
# [l, r) 
for l in range(n):
    while r < n and s+A[r] <= K:
        s += A[r]
        r += 1
    ans = max(ans, r-l)
    s -= A[l]
print(ans)
