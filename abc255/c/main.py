X, A, D, N = map(int, input().split())

if D == 0 or N == 1:
    print(abs(X-A))
    exit()
if X == A:
    print(0)
    exit()

Max = A if D < 0 else A + (D*(N-1))
Min = A if D > 0 else A + (D*(N-1))
# print(Max, Min)
if Min < X < Max:
    d = (X-A) % D
    print(min(abs(d), abs(D-d)))
elif X >= Max:
    print(abs(Max-X))
else:
    print(abs(Min-X))
