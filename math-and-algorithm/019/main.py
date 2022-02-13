from collections import Counter
N = int(input())
C = Counter(map(int, input().split()))
print(sum(v * (v-1) // 2 for v in C.values() if v >= 2))