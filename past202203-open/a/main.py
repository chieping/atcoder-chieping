A, B, C = map(int, input().split())
X = [A*B, B*C, A*C]
print(min(X), max(X))