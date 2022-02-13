N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(sum(A[i]/3+B[i]*2/3 for i in range(N)))