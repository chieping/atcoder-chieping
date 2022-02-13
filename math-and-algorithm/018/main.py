from collections import Counter
N = int(input())
C = Counter(map(int, input().split()))
print(C[100]*C[400]+C[200]*C[300])