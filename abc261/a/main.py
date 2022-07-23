L1, R1, L2, R2 = map(int, input().split())
print(max(0, min(R2, R1) - max(L1, L2)))