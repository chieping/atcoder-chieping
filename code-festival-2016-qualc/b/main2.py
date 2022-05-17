K, T = map(int, input().split())
A = list(map(int, input().split()))
Max = max(A)
print(max(0, Max - 1 - (K - Max)))