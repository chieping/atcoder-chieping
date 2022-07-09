N, M, X, T, D = map(int, input().split())
C = T - (X * D)
ans = C + min(X, M) * D
print(ans)