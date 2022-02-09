N, A, B = map(int, input().split())
C = A+B
d, r = divmod(N, C)
print(A*d+min(r, A))