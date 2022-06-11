X, A, D, N = map(int, input().split())
# Dが0以上になるように正規化する
if D < 0:
    A = A + D * (N-1)
    D = -D
if D == 0:
    print(abs(X-A))
    exit()

Min = A
Max = A + (D*(N-1))
if Min <= X <= Max:
    d = (X-A) % D
    print(min(abs(d), abs(D-d)))
elif X > Max:
    print(abs(Max-X))
else:
    print(abs(X-Min))
