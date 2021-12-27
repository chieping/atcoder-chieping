N = int(input())
num = 1<<N
A = list(map(int, input().split()))
a = max(A[:num//2])
b = max(A[num//2:])
print(A.index(min(a, b))+1)
