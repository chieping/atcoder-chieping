H, N = map(int, input().split())
A = list(map(int, input().split()))
print('Yes' if sum(sorted(A, reverse=True)[:N]) >= H else 'No')
