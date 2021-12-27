A, B = input().split()
Asum = sum(map(int, list(A)))
Bsum = sum(map(int, list(B)))
print(max(Asum, Bsum))
