N, K = map(int, input().split())
min_num = min(N % K, K-(N%K))
print(min_num)