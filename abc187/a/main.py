A, B = input().split()
Asum = sum(map(int, list(A)))
Bsum = sum(map(int, list(B)))

if Asum >= Bsum:
    print(Asum)
else:
    print(Bsum)
