N, K = map(int, input().split())
A = []
while N > 0:
    d, r = divmod(N, K)
    A.append(r)
    N = d
print(len(A))