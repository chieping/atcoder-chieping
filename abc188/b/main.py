N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = sum(A[i]*B[i] for i in range(N))

print('Yes' if result == 0 else 'No')
